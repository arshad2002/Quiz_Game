import requests

# https://opentdb.com/
# from this site the below api is collected

url = 'https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean'

try:
    # Make a GET request to the API endpoint
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request was not successful

    # Access the response data
    question_data = response.json()
    #print(question_data)

except requests.exceptions.RequestException as e:
    # Handle any request-related exceptions
    print(f"Request failed: {e}")
except KeyError as e:
    # Handle exceptions related to missing keys in the response data
    print(f"Invalid response format: {e}")
except ValueError as e:
    # Handle exceptions related to parsing the response as JSON
    print(f"Invalid JSON response: {e}")
except Exception as e:
    # Handle any other unexpected exceptions
    print(f"An error occurred: {e}")
