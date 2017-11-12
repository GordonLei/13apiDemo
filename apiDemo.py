from flask import Flask, render_template
from random import randint
import urllib2, json 

import ssl

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def root():
    return render_template("base.html")

@app.route("/NASA",  methods=['POST', 'GET'])
def NASA():
    u=urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=R3gOeQJ7wEDvbHpGcFybE6EBUU1jEITJv5e2TS4Y")
    info = u.read()
    infoDict = json.loads(info)
    imgSrc = infoDict['url']
    explanationText = infoDict['explanation']
    return render_template("NASA.html", img = imgSrc, explanation = explanationText)

        
@app.route("/hearthstone", methods=['POST', 'GET'])
def hearthstone():
    num = randint(1,123)
    if (num < 10):
        num = "00" + str(num)
    elif (num < 100):
        num = "0" + str(num)
    else:
        num = str(num)
    link = "https://omgvamp-hearthstone-v1.p.mashape.com/cards/GVG_" + num;
    print link
    req = urllib2.Request(link)
    req.add_header('X-Mashape-Key', "6xOI3T0ppJmshE6nZ3MJoiYW84OFp1Mjmg5jsnaRBcJb1Ai9Nf")
    req.add_header("Accept",  "application/json")
    resp = urllib2.urlopen(req)
    cards = resp.read()
    cardDict = json.loads(cards)
    cardName = cardDict[0]['name']
    cardSet = cardDict[0]['cardSet']
    cardImg = cardDict[0]['imgGold']
    cardFlavor = cardDict[0]['flavor']
    cardArtist = cardDict[0]['artist']
    cardID = cardDict[0]['cardId']
    return render_template("hearthstone.html", name = cardName, set = cardSet, img = cardImg, flavor = cardFlavor, artist = cardArtist, id= cardID)
    
if __name__ == '__main__':
    app.debug = True
    app.run()