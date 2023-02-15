

from pprint import pprint
from newsapi import NewsApiClient
URL = ('https://newsapi.org/v2/top-headlines?country=us')
api = NewsApiClient(api_key="bdc4bcc577c34dc194527f8c27c71208")

top_headlines = api.get_top_headlines()


for article in top_headlines['articles']:
    pprint(f"{article['title']} ({article['url']})")
