

from pprint import pprint
from newsapi import NewsApiClient
import click
import webbrowser
URL = ('https://newsapi.org/v2/top-headlines?country=us')
api = NewsApiClient(api_key="bdc4bcc577c34dc194527f8c27c71208")


print("Welcome, let's see the news")

category = 'general'
top_headlines = api.get_top_headlines(category=category)

if top_headlines is not None:
    articles = top_headlines['articles']
    for index, article in enumerate(articles):
        title = (f"{index + 1}. {article['title']}")
        click.echo(click.style(title, fg='green'))
        print()

    index = int(input("Enter the number of the article you want to read: ")) - 1
    if 0 <= index < len(articles):
        article = articles[index]
        url = article['url']
        webbrowser.open(url, new=2)
    else:
        print("Invalid article number")
