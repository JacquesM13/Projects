import requests
from datetime import datetime

USERNAME = "jacqu3s"
GRAPH_ID = "graph1"
TOKEN = "h3h312345678"

pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

# --- User creation - comment out after the fact ---

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url= pixela_endpoint, json= user_params)
# print(response.text)


# --- Graph creation - comment out after the fact ---

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "shibafu"
}

# response = requests.post(url= graph_endpoint, json= graph_config, headers= headers)
# print(response)


# today = datetime.now()
today = datetime.now()
today = today.strftime("%Y%m%d")


# --- POST - Posting event to graph ---

pixel_values = {
    "date": today,
    "quantity": "24.78",
}

# response = requests.post(url= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}", json= pixel_values, headers= headers)
# print(response.text)


# --- PUT - Updating an existing event ---

update_values = {
    "quantity": "24.79"
}

# response = requests.put(url= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}", json= update_values, headers= headers)
# print(response.text)


# --- DELETE - Deleting an existing event ---

# response = requests.delete(url= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}", headers= headers)
# print(response.text)

# --- INTERACTIVITY ---

pixel_values = {
    "date": today,
    "quantity": input("How many km did you cycle today? ")
}

response = requests.post(url= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}", json= pixel_values, headers= headers)
print(response.text)