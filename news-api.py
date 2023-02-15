

from pprint import pprint
from newsapi import NewsApiClient
import click
URL = ('https://newsapi.org/v2/top-headlines?country=us')
api = NewsApiClient(api_key="bdc4bcc577c34dc194527f8c27c71208")

print("Welcome, let's see the news")
category = input(
    "Select a news category (business, entertainment, general, health, science, sports, technology): ")
top_headlines = None

valid_categories = ['business', 'entertainment',
                    'general', 'health', 'science', 'sports', 'tecnology']
if category not in valid_categories:
    print('Invalid category. Please choose from the following categories: business, entertainment, general, health, science, sports, technology')
else:
    top_headlines = api.get_top_headlines(category=category)
if top_headlines is not None:
    for article in top_headlines['articles']:
        pprint
        for article in top_headlines['articles']:
            title = (article['title'] + "\n")
            url = article['url']
            click.echo(
                f"{title}\n{click.style  (url, fg='blue', underline=True)}\n")
