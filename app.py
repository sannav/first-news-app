# -*- coding: utf-8 -*-

# importer
from flask import Flask
from flask import render_template
app = Flask(__name__)

#  variabeln app skapa funktionen en route oot-mapp och staller sig dar
#skapa en funktion som skapar en indexfil for hemsidan där appen ska ligga, i root-mappen
@app.route("/")
def index():
    template = 'index.html'
    return render_template(template)
if __name__ == '__main__':
    # Starta Flask test server i debbuging lagege
    app.run(debug=True, use_reloader=True)
	