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
username = input("Enter a known or suspected username for further lookup (Optional): ")




"""Once we gather that information could I pivot the search and enter in new info to continue this research.. 
Then save to a doc or pdf and can put in a route to a file so I can get stuff collected together

"""

savedResults= {
    "First Name": First_Name, 
    "Last Name": Last_Name, 
    "Address": address, 
    "City": city, 
    "State": state, 
    "Phone Number": phone_number,
    "Age Range": age_range, 
    "Location": location, 
    "Birthdate": birthdate
}
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


social_lookup_links = []
if username:
    encoded_username = urllib.parse.quote(username)
    social_lookup_links = [
        f"https://namechk.com/{encoded_username}",
        f"https://www.google.com/search?q={encoded_username}",
        f"https://whatsmyname.app/?q={encoded_username}",
    ]    

filename = f"Investigation_{First_Name}_{Last_Name}.txt"
filepath = f"c:\\Users\\JamesJPDumas\\Desktop\\{filename}"
'Save this to a file /desktop'
with open(filepath, "w") as file:
    file.write("=== Information ===")
    for key, value in savedResults.items():
        file.write(f"{key}: {value}\n")
        file.write("=============================\n")

    file.write("==== Search Results ====\n")
    for site in websites:
        file.write(site + "\n")
        file.write("=============================\n")

    file.write("=== User Name ===\n \n")
    for social in social_lookup_links:
        file.write(social + "\n" )
        file.write("=============================\n")

print(f"[+] Investigation save to: {filepath}")


