import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variables
api_key = os.getenv("PROXYCURL_API_KEY")
if api_key is None:
    raise ValueError("PROXYCURL_API_KEY environment variable is not set")

# Set up the headers with the API key
headers = {"Authorization": "Bearer " + api_key}

# Define the API endpoint and parameters
api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
params = {
    "linkedin_profile_url": "https://www.linkedin.com/in/andrewyng/",
}

# Make the GET request
response = requests.get(api_endpoint, params=params, headers=headers)

# Check if the response is successful
if response.status_code == 200:
    # Overwrite the file 'response.json' with the new content
    with open("response.json", "w") as f:
        f.write(response.text)
    print("File 'response.json' has been overwritten.")
else:
    print(f"Failed to download file. Status code: {response.status_code}")
