require 'open-uri'
require 'json'
require 'nokogiri'
require 'set'

seed_url = "http://stackoverflow.com/"
max_depth = 3

# Maintain a list of URL's that we need to check
urls_to_check = [{url: seed_url, depth: 1}]

# Add all URL's checked to a set to avoid duplicating work
urls_checked = Set.new

# An index that has words pointing to pages that contain them
index = {}

until urls_to_check.empty?
  # Pop off the next url to check, and mark it as checked
  next_url = urls_to_check.pop
  urls_checked.add(next_url[:url])

  # Fetch the source code. Ignore the page if we can't fetch it correctly
  begin
    source = open(next_url[:url])
  rescue OpenURI::HTTPError, Zlib::DataError
    next
  end

  # Parse the HTML source and fetch all of the words on the page and the links
  doc = Nokogiri::HTML(source)
  links = doc.css('a')
  words_on_page = doc.content.split

  # Add all the words on the page to the index
  words_on_page.each do |word|
    index[word] ||= {}
    index[word][next_url[:url]] ||= 0
    index[word][next_url[:url]] += 1
  end

  # Get the URL's from all of the a tags that have an href
  urls = links.map{ |a| a.attributes['href'] }.compact.map{ |href| href.value }

  # Add all of the new url's to our list of pages to check if we haven't checked them already
  urls.each do |url|
    # If we have a relative url '/search' instead of 'http://google.com/search',
    # then append it to our base path
    if !url.start_with?("http")
      url = (URI.parse(next_url[:url]) + url).to_s
    end

    # If we haven't checked the URL and we aren't at our max depth, add it to our list
    if next_url[:depth] != max_depth && !urls_checked.include?(url)
      urls_to_check << {url: url, depth: next_url[:depth]+1}
    end
  end
end

# Write our index to a file
File.open('index.json', 'w') { |f| f.puts(JSON.generate(index)) }
