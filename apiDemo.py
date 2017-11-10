from flask import Flask, render_template
import urllib2, json 

import ssl

app = Flask(__name__)

@app.route("/")
def root():
    u=urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=R3gOeQJ7wEDvbHpGcFybE6EBUU1jEITJv5e2TS4Y")
    info = u.read()
    infoDict = json.loads(info)
    imgSrc = infoDict['url']
    explanationText = infoDict['explanation']
    dump(infoDict)
    return render_template("base.html", img = imgSrc, explanation = explanationText)

if __name__ == '__main__':
    app.debug = True
    app.run()