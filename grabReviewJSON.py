import requests
payload = {'filter':'recent', 'review_type':'negative','num_per_page':'100'}
response = requests.get("https://store.steampowered.com/appreviews/1454400?json=1",payload)

responseJSON = response.json()
reviews = responseJSON['reviews']
reviewList = [x['review'] for x in reviews]