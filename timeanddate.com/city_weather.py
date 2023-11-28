import requests
from bs4 import BeautifulSoup, NavigableString
import re


def fetch_weather_details(location_url):
    # Fetching the web page for the specific location
    response = requests.get(location_url)

    # Initialize a string to hold the data
    weather_details_string = ""

    # Check if the page was found
    if response.status_code != 200:
        weather_details_string += "Weather details not found for the given location.\n"
        return weather_details_string

    # Parsing the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting the necessary weather information
    location_name = location_url.split('/')[-1].replace('-', ' ').title()
    temperature = soup.find('div', class_='h2').get_text(strip=True) if soup.find('div', class_='h2') else "N/A"
    weather = soup.find('p').get_text(strip=True) if soup.find('p') else "N/A"

    # Extracting "Feels Like" information
    feels_like_element = soup.find('p', string=re.compile('Feels Like'))
    feels_like = feels_like_element.get_text(strip=True) if feels_like_element else "N/A"

    # Extracting "Forecast" information
    forecast_element = soup.find('span', title=re.compile('forecasted temperature today'))
    forecast = forecast_element.get_text(strip=True).replace('\xa0', ' ') if forecast_element else "N/A"
    forecast = forecast.replace("Forecast: ", "")

    # Extracting "Wind" information
    wind_speed = "N/A"
    wind_direction = "N/A"
    wind_element = soup.find('span', class_='comp')
    if wind_element:
        for sibling in wind_element.previous_siblings:
            if isinstance(sibling, NavigableString) and sibling.strip():
                wind_speed = sibling.strip()
                break
        wind_direction = wind_element.get('title', '')

    wind = f"{wind_speed} {wind_direction}".strip()
    wind = ' '.join(wind.split())  # Ensure there are no extra spaces

    # Adding the extracted weather information to the string
    weather_details_string += f"Location: {location_name}\n"
    weather_details_string += f"Temperature: {temperature}\n"
    weather_details_string += f"Weather: {weather}\n"
    weather_details_string += f"Feels Like: {feels_like}\n"
    weather_details_string += f"Forecast: {forecast}\n"
    weather_details_string += f"Wind: {wind}\n"

    return weather_details_string

def fetch_location_weather_urls(country_url):
    # Fetching the web page
    weather_response = requests.get(country_url)

    # Check if the page was found
    if weather_response.status_code != 200:
        print("Weather information not found for the given country.")
        return []

    # Parsing the HTML content
    soup = BeautifulSoup(weather_response.content, 'html.parser')

    # Find the number of locations using the header with "6 Locations"
    header = soup.find('th', class_='head')
    num_locations = 0
    if header:
        # Extracting the number using regular expression
        num_locations_match = re.search(r'(\d+)\sLocations', header.text)
        if num_locations_match:
            num_locations = int(num_locations_match.group(1))

    # Extracting the location weather URLs
    location_urls = []
    location_tags = soup.select('table.zebra.fw.tb-wt.va-m tr td a')
    for tag in location_tags[:num_locations]:  # Only take as many locations as found in the header
        location_path = tag['href']
        full_url = f'https://www.timeanddate.com{location_path}'
        location_urls.append(full_url)

    return location_urls
