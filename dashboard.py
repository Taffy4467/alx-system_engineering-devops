import requests
import json

# Set your Datadog API key and application key
api_key = 'YOUR_API_KEY'
app_key = 'YOUR_APP_KEY'

# Set the name of the dashboard you want to retrieve the ID for
dashboard_name = 'Your Dashboard Name'

# Define the Datadog API endpoint for retrieving all dashboards
dashboards_url = 'https://api.datadoghq.com/api/v1/dashboard'

# Set the headers with your API and application keys
headers = {
    'Content-Type': 'application/json',
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': app_key
}

# Make a GET request to retrieve all dashboards
response = requests.get(dashboards_url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response JSON
    dashboards = response.json()['dashboards']
    
    # Find the dashboard with the specified name
    for dashboard in dashboards:
        if dashboard['title'] == dashboard_name:
            dashboard_id = dashboard['id']
            print(f"The ID of the '{dashboard_name}' dashboard is: {dashboard_id}")
            break
    else:
        print(f"No dashboard found with the name '{dashboard_name}'")
else:
    print(f"Error retrieving dashboards. Status code: {response.status_code}")

