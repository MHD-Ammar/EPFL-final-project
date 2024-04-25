from flask import Flask, render_template,request,redirect
import json
import datetime

app = Flask(__name__)

today = datetime.date.today()

#Function for open file and read it
def get_page(page_name):
    html_file = open(page_name)
    content = html_file.read()
    html_file.close()
    return content
#Oben The json file that contain data of doctor Schedule
json_file = open("DB.json")
Schedule = json.load(json_file)
json_file.close()
day_schedule =[]
for item in Schedule:
    if item["day"] == str(today):
       day_schedule.append(item)

#Delete from json
@app.route("/delete")
def delete():
    id = request.args.get("id")
    for item in day_schedule:
        if item["id"] == str(id): 
            day_schedule.remove(item)
    return redirect("/")



@app.route("/")
def home_page():
    return render_template("index.html", message = day_schedule)