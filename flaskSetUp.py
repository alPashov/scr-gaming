from flask import Flask, render_template
from myScraper import links as links, soup as soup



app = Flask(__name__)

@app.route("/")
def gaming():
    return render_template('gaming.html', links = links, soup = soup)

app.run(host="0.0.0.0", port=5050)