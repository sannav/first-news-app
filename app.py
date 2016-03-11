import csv
from flask import Flask
from flask import render_template
app = Flask(__name__)

#skapa funktion for att ladda in csv, . betyder i nuvarande katalog, r=read
# skapa en variabel csv-path opppna csv-filen och skapa en lista 
def get_csv(csv_path):
    csv_file = open(csv_path, "r")
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

# funktionen nedan
@app.route("/")
def index():
    template = 'index.html'
    object_list = get_csv("./static/la-riots-deaths.csv")
    return render_template(template, object_list=object_list)

if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)