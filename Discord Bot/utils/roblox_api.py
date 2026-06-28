import requests

def get_user(query):
    if query.isdigit():
        user_id = int(query)
    else:
        r = requests.post(
            "https://users.roblox.com/v1/usernames/users",
            json={
                "usernames": [query],
                "excludeBannerUsers": False
            }
        )
        data = r.json().get("data")
        if not data:
            return None
        user_id = data[0]["id"]

    profile_resp = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
    if profile_resp.status_code != 200:
        return None
    profile = profile_resp.json()

    avatar = requests.get(
        f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={user_id}&size=420x420&format=Png"
    ).json()

    return {
        "id": profile["id"],
        "name": profile["name"],
        "display": profile["displayName"],
        "description": profile["description"],
        "created": profile["created"],
        "avatar": avatar["data"][0]["imageUrl"]
    }