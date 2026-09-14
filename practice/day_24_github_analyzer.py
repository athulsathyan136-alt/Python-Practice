# Day 24 - Bonus: GitHub Profile Analyzer
import requests

def get_user_info(username):
    """Fetch GitHub user info"""
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_user_repos(username):
    """Fetch all public repos for a user"""
    url = f"https://api.github.com/users/{username}/repos"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        return []
    except Exception:
        return []

def analyze_profile(username):
    """Analyze a GitHub profile"""
    print("=" * 50)
    print(f"🔍 ANALYZING: {username}")
    print("=" * 50)
    
    user = get_user_info(username)
    if not user:
        print(f"❌ User '{username}' not found!")
        return
    
    # Basic info
    print(f"👤 Name: {user.get('name', 'N/A')}")
    print(f"📝 Bio: {user.get('bio', 'No bio')}")
    print(f"📍 Location: {user.get('location', 'N/A')}")
    print(f"👥 Followers: {user['followers']}")
    print(f"👣 Following: {user['following']}")
    print(f"📦 Public Repos: {user['public_repos']}")
    
    # Repo analysis
    repos = get_user_repos(username)
    if repos:
        total_stars = sum(repo['stargazers_count'] for repo in repos)
        languages = {}
        for repo in repos:
            lang = repo.get('language')
            if lang:
                languages[lang] = languages.get(lang, 0) + 1
        
        print(f"\n⭐ Total Stars: {total_stars}")
        print(f"\n💻 Languages Used:")
        for lang, count in sorted(languages.items(), key=lambda x: -x[1]):
            print(f"   {lang}: {count} repos")
        
        # Most popular repo
        top_repo = max(repos, key=lambda r: r['stargazers_count'])
        print(f"\n🏆 Top Repo: {top_repo['name']} ({top_repo['stargazers_count']} stars)")
    
    print("\n" + "=" * 50)

# Test with your own profile
analyze_profile("athulsathyan136-alt")

# Compare with a famous dev
print("\n")
analyze_profile("torvalds")