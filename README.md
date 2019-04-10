# emby-cli-monitor

a basic cli monitor for emby.

I love emby but not so much the dashboard, sometimes i just want a quick overview of what's playing without all the extra stuff.

## Usage
Edit the url and key with your info. You can get an emby api key by going to your Dashboard>Advanced>Security and then you can generate a key. 

Install the requirements\
`pip3 install –upgrade -r requirements.txt`

Run the program\
`python3 embystatus.py`

It updates every 120 seconds, you can change this towards the bottom in the threading timer line. I suggest not going less then 60 seconds, it could slow things down if you make to many calls a min.

You can change the colors of each line by just changing the colors listed in each one.

##### Disclaimer
###### I’m still learning python so this will probably be refined and tweaked a lot, but I have been running it for a few months now without issue as is. 
