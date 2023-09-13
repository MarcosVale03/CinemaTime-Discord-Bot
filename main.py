# Import web scraping module & request library

from bs4 import BeautifulSoup
import requests

# Import discord library & command creation component from extension package
import discord
from discord.ext import commands


# import random

def parse_html(url):
    # Send a GET request to the URL
    # Create a BeautifulSoup object to parse the HTML content
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")


def main(token):
    # Is it necessary to enable message intents in Developer Portal?
    # Setting intents to all allows the bot to send messages.
    """""Intents allow bot developers to "subscribe" to specific events in Discord."""""
    intents = discord.Intents.all()

    # Create bot with command prefix, and intents as set above
    bot = commands.Bot(command_prefix='!', intents=intents)

    # Indicates that the bot successfully logged in from the console
    @bot.event
    async def on_ready():
        print(f"{bot.user.name} has logged in. Bot is ready!")

    # Various commands that can be executed
    @bot.command()
    async def home(ctx):

        soup = parse_html("https://letterboxd.com")

        # Find the movie titles

        film_titles = []

        img_tags = soup.find_all("img")

        for img in img_tags:
            title = img["alt"]
            film_titles.append(title)

            if len(film_titles) == 6:
                break

        # Prepare the response message

        message = "Movies on Homepage:\n\n"

        for titles in film_titles:
            message += f"```\n{titles}```"

        # Send the message to the Discord channel
        await ctx.send(message)

    @bot.command()
    async def info(ctx):

        response = "```Enter the name of a movie:\n```"
        await ctx.send(response)

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        # Wait for the user's response
        response = await bot.wait_for("message", check=check)

        title = response.content

        soup = parse_html(f"https://letterboxd.com/search/films/{title}/")

        # html = soup.findAll('div', attrs={'class':'film-poster'}) what is this for?
        html = soup.find_all('div', class_='film-poster')

        first_result = html[0]

        film_id = first_result["data-film-slug"]

        url = parse_html(f"https://letterboxd.com/film/{film_id}/")

        # Name of film
        film_name = url.find_all("img", limit=1)

        titles = []
        for img in film_name:
            title = img["alt"]
            titles.append(title)

        # Rating of film on Letterboxd
        rating = url.find('meta', {'name': 'twitter:data2'})['content']

        # Genres of film
        genre_url = f"https://letterboxd.com/film/{film_id}/genres/"
        response = requests.get(genre_url)

        soup = BeautifulSoup(response.content, 'html.parser')

        genres = soup.find_all('div', class_='text-sluglist capitalize')

        # for loop used to find the genre names in the html code and printing said genres
        message = 'Genre(s): '
        for genre in genres:
            link = genre.find('a')
            if link and '/films/genre/' in link['href']:
                genre_name = genre.text.strip().title()  # Remove leading and trailing whitespace
                genre_name = genre_name.replace(' ', ', ')
                message += genre_name

        # Synopsis of film
        synopsis = url.find('meta', property='og:description')['content']

        # Finding Director(s) of the film
        director = url.find('meta', {'name': 'twitter:data1'})['content']

        # find all the actors names in html code
        actors = url.find_all("a", class_='text-slug', limit=3)

        actor_names = 'Top actors: '

        # iterates through actor names and puts it in a message
        counter = 0
        for actor in actors:
            counter += 1
            if counter == (len(actors)):
                actor_names += actor.text + '  '
                break
            actor_names += actor.text + ',  '

        full_message = f"```Film Name: {titles[0]}\n\n" \
                       f"Rating: {rating}\n\n" \
                       f"Director(s): {director}\n\n" \
                       f"Actors: {actor_names}\n\n" \
                       f"{message}\n\n" \
                       f"Synopsis: {synopsis}\n\n```"

        await ctx.send(full_message)

    @bot.command()
    async def popular(ctx):

        response = '```Get the top 5 most popular movies of all time, this year, month, or week.\nEnter at, y, m, or w:```'
        await ctx.send(response)

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        response = await bot.wait_for("message", check=check)

        # getting the url based on user input
        if response.content == 'at':
            url = 'https://letterboxd.com/films/popular/'
        elif response.content == 'y':
            url = 'https://letterboxd.com/films/popular/this/year/'
        elif response.content == 'm':
            url = 'https://letterboxd.com/films/popular/this/month/'
        else:
            url = 'https://letterboxd.com/films/popular/this/week/'

        soup = parse_html(url)

        # Getting top 5 movies of ALL TIME
        


    bot.run(token)


# Discord bot token (found in developer portal)

user_token = "TOKEN"

main(user_token)
