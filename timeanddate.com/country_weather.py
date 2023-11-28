import requests
from bs4 import BeautifulSoup

def fetch_weather_data(country_url):
    # Fetching the web page
    weather_response = requests.get(country_url)

    # Initialize a string to hold the data
    weather_data_string = ""

    # Check if the page was found
    if weather_response.status_code != 200:
        weather_data_string += "Weather information not found for the given country.\n"
        return weather_data_string

    # Parsing the HTML content
    soup = BeautifulSoup(weather_response.content, 'lxml')

    # Finding the table that contains the weather information
    table = soup.find('table', class_='table table--left table--inner-borders-rows')

    # Check if the table was found
    if not table:
        weather_data_string += "Weather table not found.\n"
        return weather_data_string

    # Finding all 'tr' elements in the table
    tr_elements = table.find_all('tr')
    # Initialize a dictionary to hold the data
    weather_info = {}

    # Extract weather information from the table
    for tr in tr_elements:
        th = tr.find('th')
        td = tr.find('td')
        if th and td:
            header_text = th.get_text(strip=True).replace(':', '').strip()
            value_text = ' '.join(td.stripped_strings)  # This line is updated to insert space correctly.
            weather_info[header_text] = value_text

    # Add the extracted weather information to the string
    for key, value in weather_info.items():
        if 'High' in key or 'Low' in key or 'Wind' in key:
            # Insert space before the city name if missing
            value = value.replace('°C', '°C ').replace('km/h', 'km/h ')
        weather_data_string += f"{key}: {value}\n"

    return weather_data_string

def get_weather_url():
    country_input = input("Enter the country name for weather information: ")

    country_url_part = country_input.strip().replace(" ", "-").lower()
    return f'https://www.timeanddate.com/weather/{country_url_part}'
