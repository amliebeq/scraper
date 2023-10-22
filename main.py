from bs4 import BeautifulSoup
import requests
import pandas as pd

n = 1
project_managers_list = []

while n < 50:
    url = f'https://www.yellowpages.com/search?search_terms=property%20management&geo_location_terms=Mesa%2C%20AZ&refinements=headingtext%3AReal%20Estate%20Management&page={n}'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html')

    business_names = [name.text for name in soup.find_all('a', class_ = 'business-name')]
    business_addresses = [address.text for address in soup.find_all('div', class_ = 'street-address')]
    business_locality = [locality.text for locality in soup.find_all('div', class_ = 'locality')]
    business_phone_number = [phone_number.text for phone_number in soup.find_all('div', class_ = 'phones')]

    for num in range(30):
        project_managers_list.append({'name': business_names[num], 'address': business_addresses[num], 'locality': business_locality[num], 'phone_number': business_phone_number[num]})

    n += 1
    print(n)

df = pd.DataFrame(project_managers_list)

df.to_csv('property_manager_info_4.csv')