from flask import Flask, render_template,request,redirect
import json
import datetime

app = Flask(__name__, template_folder='templates')

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
        data = work_with_json("DB.json", "r")
        max_id = 0
        for item in data:
            if item['id'] > max_id:
                max_id = item['id']
        sent_data = {"name": self.patient_name,
        "phone": self.phone,
        "compleain":self.compleain,
        "date": self.date,
        "time_slot": self.time_slot ,
        "id": (max_id +1)}
        data.append(sent_data)
        json_file = open("DB.json", "w")
        json.dump(data, json_file)
        json_file.close()



    

#function for open json file
def work_with_json(file_name,status):
        json_file = open(file_name, status)
        data = json.load(json_file)
        json_file.close()
        return data
    

#Function for open file and read it
def get_page(page_name):
    html_file = open(page_name)
    content = html_file.read()
    html_file.close()
    return content
#Oben The json file that contain data of doctor Schedule
Schedule = work_with_json("DB.json", "r")
day_schedule =[]
for item in Schedule:
    if item["date"] == str(today):
       day_schedule.append(item)

#Delete from json
@app.route("/delete")
def delete():
    id = request.args.get("id")
    for item in day_schedule:
        if item["id"] == int(id):
            day_schedule.remove(item)
    return redirect("admin")

@app.route("/date")
def date():
    day_time = []
    date = request.args.get("d")
    Schedule = work_with_json("DB.json", "r")
    for item in Schedule:
        if item["date"] == date:
            day_time.append(item["time_slot"])
    

    return render_template( "index.html" , time_slot = day_time)




@app.route("/admin")
def home_page():
    return render_template("schedule.html", message = day_schedule)

@app.route("/")
def register_page():
    Schedule = work_with_json("DB.json", "r")
    return render_template("index.html" , today = str(today))

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