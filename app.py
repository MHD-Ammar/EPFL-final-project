from flask import Flask, render_template, request, redirect #import flask
import json #import json
import datetime #import datetime
# python -m flask --app app.py --debug run
app = Flask(__name__, template_folder='templates')

#use datetime to know the date of today
today = datetime.date.today()

# Class definition to save the input of the user in Jsone file
class patient:
    # initialize the object
    def __init__ (self, patient_name, phone, compleain, date, time_slot):
        self.patient_name = patient_name
        self.phone = phone
        self.compleain = compleain
        self.date = date 
        self.time_slot = time_slot
    # method to store the data frome user in json file 
    def store(self):
        data = work_with_json("DB.json", "r")
        max_id = 0 
    
        #check the biges id 
        for item in data:
            if item['id'] > max_id:
                max_id = item['id']
        sent_data = {"name": self.patient_name,
        "phone": self.phone,
        "compleain":self.compleain,
        "date": self.date,
        "time_slot": self.time_slot ,
        "id": (max_id +1)}
    
        #append the data in the json file
        data.append(sent_data)
        json_file = open("DB.json", "w")
        json.dump(data, json_file)
        json_file.close()
    
        #method to sed the username and greeting thim after register
    def greeting(self):
        greeting_page = open("templates/greeting.html")
        content = greeting_page.read()
        greeting_page.close()
        times = {"1":"09:00","2":"09:30","3":"10:00","4":"10:30","5":"11:00","6":"11:30","7":"12:00","8":"12:30","9":"01:00","10":"01:30","11":"02:00","12":"02:30"}
        return content.replace("$$name$$",self.patient_name).replace("$$compleain$$",self.compleain).replace("$$time$$",(times[self.time_slot]))

#function for open json file
def work_with_json(file_name, status):
        json_file = open(file_name, status)
        data = json.load(json_file)
        json_file.close()
        return data
    
#Oben The json file that contain data of doctor Schedule
Schedule = work_with_json("DB.json", "r")
day_schedule =[]
# make list that contain today scedule
for item in Schedule:
    if item["date"] == str(today):
       day_schedule.append(item)


#route home page
@app.route("/")
def home():
    return render_template("index.html")

#Delete from daly schedule when the doctor fished t
@app.route("/delete")
def delete():
    id = request.args.get("id")
    for item in day_schedule:
        if item["id"] == int(id):
            day_schedule.remove(item)
    return redirect("schedule")
#display only the unbooked time slot
@app.route("/date")
def date():
    day_time = []
    date = request.args.get("d")
    Schedule = work_with_json("DB.json", "r")
    for item in Schedule:
        if item["date"] == date:
            day_time.append(item["time_slot"])
    return render_template( "register.html" , time_slot = day_time)

#route to the register page
@app.route("/register")
def register_page():
    return render_template("register.html" , today = str(today)) # sent today to prevint to select old date
#rout to greating page and seve the data in opject of class
@app.route("/greeting")
def reg():
    name = request.args.get("name")
    phone = request.args.get("phone")
    compleain = request.args.get("compleain")
    date = request.args.get("date")
    time_slot = request.args.get("time_slot")
    patient_data = patient(name, phone, compleain, date, time_slot)
    patient_data.store() 
    return patient_data.greeting()

# to load the doctor schedule
@app.route("/schedule")
def schedule_page():
    return render_template("schedule.html", message = day_schedule)
#rout the admin page
@app.route("/admin")
def login_page():
    return render_template("admin.html")
#check if the passored is corect to veiw the doctor schedule
@app.route("/check") 
def check_login():
    username = request.args.get("username")
    password = request.args.get("password")
    if username == "doctor" and password == "topsecret":
        return redirect("/schedule")
    else:
        return redirect("/admin")
   
        


