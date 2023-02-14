
from datetime import datetime
from pprint import pprint
from newsapi import NewsApiClient
URL = ("https://newsapi.org/v2/everything?q=Nba&sortBy=popularity")
api = NewsApiClient(api_key="bdc4bcc577c34dc194527f8c27c71208")

response = api.get_everything(q='nba', sources='reuters')


pprint(response['articles'])
