require 'open-uri'
require 'nokogiri'

BASE_URL = 'http://bulbapedia.bulbagarden.net'

# Fetch the pokemon list page and parse it with nokogiri
source = open("#{BASE_URL}/wiki/List_of_Pok%C3%A9mon_by_base_stats")
doc = Nokogiri::HTML(source)

# Get the rows containing the pokemon information
rows = doc.css('table.roundy tr')[1..-1]

rows.each do |row|
  # Get the number and name from the td cells content
  cells = row.children.css('td')
  number = cells[0].content.chomp
  name = cells[2].content.chomp
  # Get the URL for the pokemon's page by getting the href from the a element
  url = BASE_URL + cells[2].children.css('a')[0].attributes['href'].value
  puts "#{number} #{name} #{url}"
end
