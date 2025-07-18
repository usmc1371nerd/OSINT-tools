import webbrowser
import urllib.parse
  
  
"""
Todo: - Add error handling for user inputs
      - Add more websites to search
      - Add functionality to save results to a file
      - Add functionality to scrape results from the websites
      - Add some free APIs to search for people/domains/and etc
      - Add functionality to search for people by email
      - Add functionality to search for people by phone number
      
"""  
  
  
    
# This script searches for a specific website in a list of websites and prints the result.
First_Name = input('Enter the targets first name:(Required) ')
Last_Name = input('Enter the targets last name:(Required) ')
name = f"{First_Name} {Last_Name}"
name_spokeo = f"{First_Name}-{Last_Name}"
address = input('Enter the targets street address: (Optional leave blank hit enter) ')
city = input('Enter the targets city: (Required) ')
state = input('Enter the targets state: (Optional leave blank hit enter) ')
age_range = input('Enter the targets age range: (For people searches that require age ranges you must enter in these formatted ranges 18-25 26-39 40-49 50-59 60+) ')
location = f"{city}, {state}" 
birthdate = input('Enter the targets birthdate: (Optional leave blank hit enter) ')
phone_number = input('Enter the targets phone number: (Optional leave blank hit enter) ')


"""Once we gather that information could I pivot the search and enter in new info to continue this research.. 
Then save to a doc or pdf and can put in a route to a file so I can get stuff collected together

"""


results = f"{name} {location} {birthdate}"
results = urllib.parse.quote(results)
websites = [
    'https://www.google.com/search?q=' + results,
    'https://www.bing.com/search?q=' + results,
    'https://yandex.com/search/?text=' + results,
    'https://www.duckduckgo.com/?q=' + results,
    f'https://www.spokeo.com/search/{name_spokeo}?age_range={age_range}&city={city}&phone={phone_number}&state={state}'
    f'https://www.thisnumber.com/{phone_number}' 
    'https://www.whitepages.com/name/' + name + '/' + location,
    'https://www.anywho.com/people' + name + '/' + location,
    
]



for site in websites:
    webbrowser.open_new_tab(site)
