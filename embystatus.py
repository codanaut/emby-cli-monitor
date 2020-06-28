import requests
import json
from termcolor import colored
import threading
import os

url ="http://0.0.0.0:8096"   
key ="your key"

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
    x = activeCount
    devicecount = len(activeCount)

    n = 0
    for device in activeCount:
        try:
            vType = device['NowPlayingItem']['Type']
            n += 1
            
        except KeyError:
            pass


    print(colored("##############################", 'green'))
    print("Emby Status" + " " + "(V " + version + ")")
    print("-----------")
    print(colored("Users - ", 'red') + str(usercount) + " " + colored("Active Devices - ", 'red') + str(devicecount))
    print("------------------------------")
    print(colored("Tv Shows - ", 'red') + shows + " " + colored("Movies - ", 'red') + movies)
    print(colored("##############################", 'green'))
    print(colored("Active Streams: ", 'red') + str(n))

    for user in x:
        try:
            client = user['UserName']
            
            vType = user['NowPlayingItem']['Type']

            if vType == "Movie":
                episode = user['NowPlayingItem']['Name']

                print(colored("##############################", 'green'))
                print(colored("User: ",'red') + client)
                print(colored(vType, 'red') + colored(": ", 'red') + episode)
                #print(colored("##############################", 'green'))

            elif vType == "Episode":
                show = user['NowPlayingItem']['SeriesName']
                episode = user['NowPlayingItem']['Name']

                print(colored("##############################", 'green'))
                print(colored("User: ",'red') + client)
                print(colored("Show: ", 'red') + show)
                print(colored("Episode: ", 'red') + episode)
                #print(colored("##############################", 'green'))


        except KeyError:
            pass

def run():
    threading.Timer(120, run).start()
    print("running thread")
    os.system('cls' if os.name == 'nt' else 'clear')
    status()
    print(colored("##############################", 'green'))

run()