require 'json'

# Load in our index file
index = JSON.parse(File.open('index.json').read)

loop do
  print "Lookup Word: "
  word = gets.chomp

  # Loop up the search word
  # Sort it by the number of times it shows up on the page (Reverse for largest first)
  # And print out each url
  index[word].sort_by{|k,v| v}.reverse.each do |result|
    puts result[0]
  end
end
