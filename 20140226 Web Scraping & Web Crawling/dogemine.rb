require 'mechanize'
require 'io/console'

# Get the username and password from the user
print "Username: "
username = gets.chomp
print "Password: "
# Don't display the password the user enters
password = STDIN.noecho(&:gets).chomp
puts

agent = Mechanize.new

# Fetch the login page, enter the username and password and submit the form (login)
agent.get("https://dogehouse.org/?page=login")
form = agent.page.forms[0]
form['username'], form['password'] = username, password
form.submit

# Fetch the dashboard page, and get the table rows containing loda information
agent.get("https://dogehouse.org/?page=dashboard")
rows = agent.page.parser.css('.stratumtable table tr')

# Iterate through the table rows and find the lowest Lowdiff port
minimum = nil
minimum_port = nil
1.upto(rows[0].children.length-1) do |i|
  name = rows[0].children[i].content
  value = rows[1].children[i].content
  if name[0] == 'L'
    if minimum.nil? || value < minimum
	  minimum = value
	  minimum_port = name[2..-1]
    end
  end
end

# Get the URL's from the gettingstarted page and find the one that corresponds to our minport
agent.get("https://dogehouse.org/?page=gettingstarted")
urls = agent.page.parser.css('.module_content > li > table > tbody > tr kbd').map(&:content)
puts urls.find { |url| url.end_with?(minimum_port) }
