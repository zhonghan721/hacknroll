# LocatorHackerBot

## Inspiration
Finding the nearest restaurant can be difficult especially we are visiting an area for the first time. 

## What it does
LocatorHackerBot is a Telegram bot that helps users locate the 10 nearest places of interest in their area. Users can input their live location and search category, and the bot will provide a list of desired destinations along with their distance and duration from the user’s location.

## How we built it
* Getting user's live location and search category from Telegram Bot
* Find the closest match to Google's predefined places categories using spaCy similarity_score function
* Feeding the location and category into google-places API to generate the list of desired destinations
* Using google-distance-matrix API to generate the distance and duration to those destinations

## Challenges we ran into
* Learning how to use APIs for Telegram Bot and Google Maps was difficult as they are completely foreign to us. 
* There are also many ways to host the bot on free servers but was too complicated for us to make it work. Hence the bot can only live on our own local server.
* Erroneous input by users leads to inaccuracy in the results returned as we use Python spaCy to parse user input and match with Google Places' predefined categories.

## Accomplishments that we're proud of
We are proud of building our first hackathon project and creating a Telegram bot that works.

## What we learned
We learned how to use Telegram APIs, Google Maps APIs, and Python.

## What's next for LocatorHackerBot
Our next step is to change the codebase such that it can be hosted on an online server. This will allow us to make the bot accessible to a wider audience and improve its functionality.
