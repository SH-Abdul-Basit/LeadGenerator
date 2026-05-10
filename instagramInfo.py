import instaloader

L = instaloader.Instaloader()

target_username = "natgeo"

profile = instaloader.Profile.from_username(L.context, target_username)

print(profile)

# HEADERS = {
#     "X-IG-App-ID": "936619743392459",
#     "X-ASBD-ID": "198387",
#     "User-Agent": (
#         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
#         "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
#     ),
# }
#
# def fetch_profile(L: instaloader.Instaloader, username: str) -> instaloader.Profile:
#     try:
#         return instaloader.Profile.from_username(L.context, username)
#     except instaloader.exceptions.ProfileNotExistsException:
#         pass
#     url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"
#     headers = {**HEADERS, "Referer": f"https://www.instagram.com/{username}/"}
#     resp = L.context._session.get(url, headers=headers, timeout=L.context.request_timeout)
#     if resp.status_code == 404:
#         raise instaloader.exceptions.ProfileNotExistsException(f"Profile {username} does not exist.")
#     resp.raise_for_status()
#     user = (resp.json().get("data") or {}).get("user")
#     if not user:
#         raise instaloader.exceptions.ProfileNotExistsException(f"Profile {username} does not exist.")
#     return instaloader.Profile(L.context, user)
#
#
# L = instaloader.Instaloader()
#
# data = fetch_profile(L, "@natgeo")
#
# print(data)