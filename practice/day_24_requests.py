# Day 24: APIs with requests
import requests
import json

print("=" * 40)
print("1. SIMPLE GET REQUEST")
print("=" * 40)

# Fetch a random joke
response = requests.get("https://official-joke-api.appspot.com/random_joke")
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    print(f"Setup: {data['setup']}")
    print(f"Punchline: {data['punchline']}")
else:
    print("Failed to fetch joke.")

print("\n" + "=" * 40)
print("2. GITHUB USER INFO (JSON Parsing)")
print("=" * 40)

username = "athulsathyan136-alt"
url = f"https://api.github.com/users/{username}"

response = requests.get(url)

if response.status_code == 200:
    user = response.json()
    print(f"Name: {user.get('name', 'N/A')}")
    print(f"Bio: {user.get('bio', 'N/A')}")
    print(f"Public Repos: {user['public_repos']}")
    print(f"Followers: {user['followers']}")
    print(f"Location: {user.get('location', 'N/A')}")
else:
    print(f"User not found. Status: {response.status_code}")

print("\n" + "=" * 40)
print("3. POST REQUEST (Sending Data)")
print("=" * 40)

# Post data to httpbin (a testing API)
payload = {
    "name": "Athul Sathyan",
    "role": "Cloud AI Engineer",
    "skills": ["Python", "AWS", "LangChain"]
}

response = requests.post("https://httpbin.org/post", json=payload)

if response.status_code == 200:
    result = response.json()
    print("Data sent successfully!")
    print(f"Server received: {json.dumps(result['json'], indent=2)}")

print("\n" + "=" * 40)
print("4. ERROR HANDLING WITH REQUESTS")
print("=" * 40)

def fetch_url(url):
    """Safely fetch a URL and return response or error"""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raises exception for 4xx/5xx errors
        return response.json()
    except requests.exceptions.Timeout:
        return "Error: Request timed out"
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect"
    except requests.exceptions.HTTPError as e:
        return f"HTTP Error: {e}"
    except Exception as e:
        return f"Unknown error: {e}"

# Test with valid URL
result = fetch_url("https://api.github.com/users/torvalds")
print(f"Linus Torvalds repos: {result['public_repos']}")

# Test with invalid URL
result = fetch_url("https://api.github.com/users/this-user-does-not-exist-xyz")
print(f"Fake user: {result}")

print("\n" + "=" * 40)
print("5. CUSTOM HEADERS")
print("=" * 40)

# Many APIs require headers (like User-Agent)
headers = {
    "User-Agent": "AthulPythonPractice/1.0",
    "Accept": "application/json"
}

response = requests.get(
    "https://api.github.com/repos/python/cpython",
    headers=headers
)

if response.status_code == 200:
    repo = response.json()
    print(f"Repo: {repo['full_name']}")
    print(f"Stars: {repo['stargazers_count']:,}")
    print(f"Language: {repo['language']}")