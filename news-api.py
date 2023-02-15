

from pprint import pprint
from newsapi import NewsApiClient
import click
URL = ('https://newsapi.org/v2/top-headlines?country=us')
api = NewsApiClient(api_key="bdc4bcc577c34dc194527f8c27c71208")

top_headlines = api.get_top_headlines()


for article in top_headlines['articles']:
    pprint
    for article in top_headlines['articles']:
        title = (article['title'] + "\n")
        url = article['url']
        click.echo(
            f"{title}\n{click.style  (url, fg='blue', underline=True)}\n")
