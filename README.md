# emby-cli-monitor

a basic cli monitor for emby.

[GUI Version Here](https://github.com/codanaut/emby-monitor)

I love emby but not so much the dashboard, sometimes i just want a quick overview of what's playing without all the extra stuff.

![alt text](https://i.imgur.com/D25bltg.png)

## Usage
Edit the url and key with your info. You can get an emby api key by going to your Dashboard>Advanced>Security and then you can generate a key. 

Install the requirements\
`pip3 install –upgrade -r requirements.txt`

Run the program\
`python3 embystatus.py`

It updates every 120 seconds, you can change this towards the bottom in the threading timer line. I suggest not going less then 60 seconds, it could slow things down if you make to many calls a min.

## Changes
- added playback status
- added easier way to change colors of each section

##### Disclaimer
###### I’m still learning python so this will probably be refined and tweaked a lot, but I have been running it for a few months now without issue as is. 
