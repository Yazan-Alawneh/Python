import requests
from bs4 import BeautifulSoup

def fetch_country_data(time_url):
    # Fetching the web page
    time_response = requests.get(time_url)

    # Parsing the HTML content
    t = BeautifulSoup(time_response.content, 'lxml')

    # Finding the table that contains the country information
    table = t.find('table', class_='table table--left table--inner-borders-rows')

    # Initialize a string to hold the data
    data_string = ""

    # Check if the table was found
    if table:
        # Finding all 'th' elements in the table
        th_elements = table.find_all('th')
        # Initialize a dictionary to hold the data
        country_info = {}

        # Find the 'th' elements for 'Country', 'Long Name', etc.
        for th in th_elements:
            header_text = th.get_text(strip=True)
            # ... existing code to extract data ...

        # Checking if we found all information and adding to data_string
        if all(key in country_info for key in ['Country', 'Long Name', 'Abbreviations', 'Capital', 'Time Zones', 'Dial Code']):
            data_string += f"Country: {country_info['Country']}\n"
            data_string += f"Long Name: {country_info['Long Name']}\n"
            data_string += f"Abbreviations: {country_info['Abbreviations']}\n"
            data_string += f"Capital: {country_info['Capital']}\n"
            data_string += f"Time Zones: {country_info['Time Zones']}\n"
            data_string += f"Dial Code: {country_info['Dial Code']}\n"
        else:
            data_string += "Some information could not be found.\n"
    else:
        data_string += "Country not found.\n"

    return data_string