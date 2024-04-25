from flask import Flask, render_template,request,redirect
import json
import datetime

app = Flask(__name__)
today = datetime.date.today()

# Class definition to save the input of the user in Jsone file
class patient:

    def __init__ (self, patient_name, phone, compleain, date, time_slot):
        self.patient_name = patient_name
        self.phone = phone
        self.compleain = compleain
        self.date = date 
        self.time_slot = time_slot
    
    def store(self):
        json_file = open("DB.json", "r")
        data = json.load(json_file)
        json_file.close()
        sent_data = {"name": self.patient_name,
        "phone": self.phone,
        "compleain":self.compleain,
        "date": self.date,
        "time_slot": self.time_slot ,
        "id": "1"}
        data.append(sent_data)
        json_file = open("DB.json", "w")
        json.dump(data, json_file)
        json_file.close()

    

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
    if item["date"] == str(today):
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

@app.route("/register")
def register_page():
    return get_page("templates/register.html")
@app.route("/registered")
def reg():
    name = request.args.get("name")
    phone = request.args.get("phone")
    compleain = request.args.get("compleain")
    date = request.args.get("date")
    time_slot = request.args.get("time_slot")
    patient_data = patient(name, phone, compleain, date, time_slot)
    patient_data.store() 
    
    return "done"