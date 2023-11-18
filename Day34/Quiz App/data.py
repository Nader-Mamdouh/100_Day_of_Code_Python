import requests as api
response = api.get(url="https://opentdb.com/api.php?amount=10&category=18&type=boolean")
api_data = response.json()
question_data = api_data["results"]
