# CinemaTime-Discord-Bot
Cinema Time is a discord bot that integrates the Letterboxd application that carries out miscellaneous tasks.

The bot uses a python library known as Beautiful Soup for webscraping capabilities. By parsing HTML code
from the website, the bot can display information for the user depending on their input.

**As of now, these are the working commands:**

  `!home` - Allows user to see the movies on the homepage of Letterboxd.

  `!info` - Prompts user to input any movie they'd like. Then displays information on said movie (Name, Director, Rating, Top 3 Actors, and Synopsis).

   `!userfav` - Prompts user to input a Letterboxd username and displays that users four favorite films. 

   `!activity` - Shows a Letterboxd users recent activity (when user watches, rates a movie, add a movie to their planning, etc.).


**In progress:**

  `!popular` - Prompts user to input a time period (all time, this year, this month, this week) and displays some of the top movies from that period.
               I believe this requires JavaScript, so this command is on hold right now. 

**Ideas to be implemented:**

  `Recommendation` - Allows user to input a movie they like so the bot can display movies similar to it based on genre.

  `Combine Letterboxd User commands` - I want to implement a menu where the user can choose what to do after entering a Letterboxd username. Since
  I will have 2 or 3 commands using a Letterboxd users profile, I can combine them into a cleaner command

  `General Ideas` - I want to clean up the program a bit. It is messy and a little inconsistent. I want to see how I could add some classes in here to clean it up
  and more functions to save space and clean up the program. I could add some files as well.
