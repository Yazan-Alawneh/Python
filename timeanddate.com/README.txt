Country Timezone and Weather Information Scraping Tool

---------------------------------------------
Overview

This Python tool allows users to enter a country name and generates a .txt file with detailed timezone and weather information for all cities in that country. The application uses web scraping techniques to gather data from specific web sources.

---------------------------------------------
Files

timezone.py: Fetches country-specific data, including time zones, capital, dial code, etc., from a time zone website.

country_weather.py: Retrieves general weather data for the input country from a weather website.

city_weather.py: Provides detailed weather information for individual cities in the specified country.

main.py: The main script that integrates other modules. It prompts the user for a country name, executes the data fetching processes, and writes the results to a text file named after the country.

---------------------------------------------
How to Use

Run main.py.
Enter the name of the country for which you want timezone and weather data.
The tool will create a .txt file named after the country. This file will contain information about the country's timezone, general weather, and detailed weather data for its cities.

---------------------------------------------
Requirements

requests library for Python
beautifulsoup4 library for Python

---------------------------------------------
Notes

Ensure you have an active internet connection as the tool fetches data online.
The accuracy of data depends on the source website's current information.
This tool is for educational purposes and might be subject to limitations based on the website's terms of use.

---------------------------------------------
Disclaimer

The tool relies on external websites for data. The developers of this tool are not responsible for the accuracy or reliability of the data provided by these external sources.