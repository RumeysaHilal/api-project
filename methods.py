import requests
import pandas as pd

def get_all_countries(base_url):
    try:
        # Send a GET request to the API
        response = requests.get(base_url)

        # If a successful HTTP response is received, proceed
        if response.status_code == 200:
            # Convert JSON data to Python objects
            countries = response.json()
            return countries
        else:
            print(f"Unable to retrieve countries. Error code: {response.status_code}")
            return None

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def create_countries_dataframe(country_data):
    # Create an empty list for the DataFrame
    data_list = []

    for country in country_data:
        country_info = {
        'Country': country.get('name', {}).get('common', 'Not Available'),
        'Capital': country.get('capital', ['Not Available'])[0],
        'Population': country.get('population', 'Not Available'),
        'Area': country.get('area', 'Not Available'),
        'Region': country.get('region', 'Not Available'),
        'Subregion': country.get('subregion', 'Not Available'),
        'Languages': ', '.join(country.get('languages', {}).values()) if 'languages' in country and country['languages'] else 'Not Available'
        }
        data_list.append(country_info)
    # Create a DataFrame
    df = pd.DataFrame(data_list)
    return df