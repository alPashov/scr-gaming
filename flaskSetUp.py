from flask import Flask, render_template
import webbrowser
from allPagesScr import main as scr

links = scr()

app = Flask(__name__)

@app.route("/")
def gaming():
    return render_template('index.html', links = links)

if __name__ == "__main__":
    webbrowser.open_new_tab("localhost:5050")
    app.run(host="0.0.0.0", port=5050)