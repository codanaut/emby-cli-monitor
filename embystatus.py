import requests
import json
from termcolor import colored
import threading
import os
import datetime

#Input your url and key here
url ="http://0.0.0.0:8096"   
key ="your key"

# amount of time to wait between updating stats in seconds.
syncTime = "120"

# coloring of different parts
breakcolor = 'green'
textColor = 'blue'
titleColor = 'red'

def status():
    #move/tv show count
    response = requests.request("GET", "%s/emby/Items/Counts?api_key=%s" % (url,key))
    data = response.json()
    movies = str(data['MovieCount'])
    shows = str(data['SeriesCount'])

    #user count
    usersresponse = requests.request("GET", "%s/emby/Users?api_key=%s" % (url,key))
    users = usersresponse.json()
    usercount = len(users)

    #version
    getSystemInfo = requests.request("GET", "%s/emby/System/Info?api_key=%s" % (url,key))
    systemInfo = getSystemInfo.json()
    version = systemInfo['Version']

    #Sessions - active streams & device count
    getDevicecount = requests.request("GET", "%s/emby/Sessions?api_key=%s" % (url,key))
    activeCount = getDevicecount.json()
    devicecount = len(activeCount)

    # count active streams
    streamCount = 0
    for device in activeCount:
        try:
            vType = device['NowPlayingItem']['Type']
            streamCount += 1
            
        except KeyError:
            pass
    
    # start printing out server information & number of active streams
    print(colored("##############################", breakcolor))
    print(colored("Emby Status (V. {})",textColor).format(version))
    print("------------------------------")
    print(colored("Users - ", titleColor) + colored(usercount,textColor) + " " + colored("Active Devices - ", titleColor) + colored(devicecount,textColor))
    print("------------------------------")
    print(colored("Tv Shows - ", titleColor) + colored(shows,textColor) + " " + colored("Movies - ", titleColor) + colored(movies,textColor))
    print(colored("##############################", breakcolor))
    print(colored("Active Streams: ", titleColor) + colored(streamCount,textColor))

    # check each active device and print out info if playing media, skip if not playing anything
    for user in activeCount:
        try:
            client = user['UserName']
            
            vType = user['NowPlayingItem']['Type']

            # check if playing or paused
            if user['PlayState']['IsPaused'] == True:
                playState = "Paused"
            
            elif user['PlayState']['IsPaused'] == False:
                playState = "Playing"

            # get play position
            runtimeTicks = user['NowPlayingItem']['RunTimeTicks']
            currentPosistionTicks = user['PlayState']['PositionTicks']

            # convert runtime ticks
            runTimeSeconds = runtimeTicks / 10000000 / 60
            runTime = str(datetime.timedelta(seconds=runTimeSeconds)).split('.', 2)[0].split(':',3)
            runTime = runTime[1]+ ":" +runTime[2]
            
            # convert current posistion ticks
            currentTimeSeconds = currentPosistionTicks / 10000000 / 60
            currentTime = str(datetime.timedelta(seconds=currentTimeSeconds)).split('.', 2)[0].split(':',3)
            currentTime = currentTime[1] + ":" + currentTime[2]
            
            
            # If Movie
            if vType == "Movie":
                episode = user['NowPlayingItem']['Name']

                print(colored("##############################", breakcolor))
                print(colored("User: ",titleColor) + colored(client,textColor))
                print(colored(vType + ": ", titleColor) + colored(episode, textColor))
                print(colored("Status: ",titleColor) + colored(playState,textColor) + " " + colored(str(currentTime) + "/" + str(runTime),textColor))
                
            # If Tv Show
            elif vType == "Episode":
                show = user['NowPlayingItem']['SeriesName']
                episode = user['NowPlayingItem']['Name']
                seasonNumber = str(user['NowPlayingItem']['ParentIndexNumber'])
                episodeNumber = str(user['NowPlayingItem']['IndexNumber'])

                print(colored("##############################", breakcolor))
                print(colored("User: ",titleColor) + colored(client,textColor))
                print(colored(vType + ": ", titleColor) + colored(episode, textColor))
                print(colored("Show: ", titleColor) + colored(show, textColor))
                print(colored("Season: ", titleColor) + colored(seasonNumber,textColor) + " " + colored("Episode: ", titleColor) + colored(episodeNumber,textColor))
                print(colored("Status: ",titleColor) + colored(playState,textColor) + " " + colored(str(currentTime) + "/" + str(runTime),textColor))
                

        # if error or not tv show or movie then pass and keep going
        except KeyError:
            pass

# Run the entire thing
def run():
    threading.Timer(int(syncTime), run).start()
    print("running thread")
    os.system('cls' if os.name == 'nt' else 'clear')
    status()
    print(colored("##############################", breakcolor))

run()
