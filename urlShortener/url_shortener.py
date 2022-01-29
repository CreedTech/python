import requests

# making using of bitly.com authentication in the url shortener
# username and password is required
username = "lazyprogrammer"
password = "creedTemmy04"

# get access token
auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token",
                         auth=(username, password))
if auth_res.status_code == 200:
    # if response is OK, get the access token
    # else print error message and exit program
    access_token = auth_res.content.decode()
    print("[!] Got access token:", access_token)
else:
    print("[!] Cannot get access token, exiting...")
    exit()

# construct the request headers with authorization
headers = {"Authorization": f"Bearer {access_token}"}

# get the group uid associated with our account
groups_res = requests.get("https://api-ssl.bitly.com/v4/groups",
                          headers=headers)
if groups_res.status_code == 200:
    # if response is OK, get the UID
    groups_data = groups_res.json()['groups'][0]
    guid = groups_data['guid']
else:
    print("[!] Cannot get GUID, exiting...")
    # exit()

# getting the url to be shortened
url = input("Enter Your url to be shortened: ")
# make the POST request to get shortened URL for url
shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", 
                            json={"group_guid": guid, "long_url": url},
                            headers=headers)
# if response is OK, get the shortened URL
# else print error
if shorten_res.status_code == 200:
    link = shorten_res.json().get("link")
    print("Shortened URL:", link)
else:
    print("Error in validating link")
