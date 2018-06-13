# YOUTUBE JUKEBOX DJANGO APP FOR SLACK
DJANGO JUKEBOX APP : A Simple youtube jukebox in django 

Configuration Steps

IN YOUR SLACK ACCOUNT


1) Create an app with a bot feature enabled,turn on bot visible always option.

2) Note the authorization key "Bot User OAuth Access Token".It will be used in the coming steps.

3) Install the app to your workspace.

4)Add the bot to the channel in which you wish to have your youtube links extracted from.

DJANGO CONFIGURATION

1) Install modules websocket,requests using pip

2) Open mychannel/chat/management/commands/connect_soc.py and replace "xxx" with
your Bot User OAuth Access Token in the payload={"token":"xxx"} 

3) Save and quit.

4) Run python manage.py connect_soc

5) Post youtube video links into the chat/channel which your bot is added to.

6) Open the HOME PAGE of the app --->  /chat/contact/


