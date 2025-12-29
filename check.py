import requests

APP_ID = ""  # your Adzuna App ID
APP_KEY = ""  # your Adzuna App Key

url = "https://api.adzuna.com/v1/api/jobs/gb/search/1"  # 'gb' for UK, change to 'us', 'in', etc.

params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "what": "Python Developer",
    "results_per_page": 3,
    "content-type": "application/json"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("✅ Connection Successful!")
    print("Total Results:", data.get("count", 0))
    for job in data.get("results", []):
        print(f"- {job['title']} at {job['company']['display_name']}")
else:
    print("❌ Connection Failed:", response.status_code)
    print(response.text)

