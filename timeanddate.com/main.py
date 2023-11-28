from timezone import fetch_country_data
from country_weather import fetch_weather_data
from city_weather import fetch_weather_details, fetch_location_weather_urls


def main():

    # Get the country name input from the user
    country_input = input("Enter the country name for weather and time zone information: ")
    filename = country_input.strip().replace(" ", "_").lower() + ".txt"

    with open(filename, 'w') as file:
        country_url_part = country_input.strip().replace(" ", "-").lower()

        # Fetch the country's timezone and other information
        time_url = f'https://www.timeanddate.com/time/zone/{country_url_part}'
        country_data = fetch_country_data(time_url)
        if country_data is not None:
            file.write(country_data + '\n\n')
        else:
            file.write("Country data not available.\n\n")

        # Fetch and write the weather information
        weather_url = f'https://www.timeanddate.com/weather/{country_url_part}'
        weather_data = fetch_weather_data(weather_url)
        file.write(weather_data + '\n\n')

        # Fetch and write detailed weather data for cities
        location_urls = fetch_location_weather_urls(weather_url)
        for url in location_urls:
            city_weather = fetch_weather_details(url)
            file.write(city_weather + '\n\n')


if __name__ == "__main__":
    main()