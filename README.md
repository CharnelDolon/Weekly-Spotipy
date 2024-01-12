# Saved-Weekly-Script
Developed Spotify Python Script using Flask and spotipy.py library to saves a user's "Discover Weekly" playlist every week. 

{WIP} Automated Weekly update feature: Currently the script is running on localhost server and is unable to work when primary PC is turned off. Working on scheduled interval functionality for the script so that runs at all times. I am experimenting different ways to implement this feature, but my plan so far is put script through AWS Lambda function behind API gateway and a Eventbridge trigger set to weekly for free automation. 
