import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"limit": 10}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            
            for post in data["data"]["children"]:
                print(post["data"]["title"])
        else:
            print("None")
    
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

top_ten("python")
