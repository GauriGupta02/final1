from flask import Flask, render_template, request, redirect, url_for
from reminder import MedicineReminder
from scheduler import start_scheduler, send_email

app = Flask(__name__)
reminder_manager = MedicineReminder()

start_scheduler(reminder_manager)  


@app.route("/", methods=["GET", "POST"])
def medication():
    if request.method == "POST":

        return redirect(
            url_for("index")
        )  

    return render_template("medication.html")


@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        med_name = request.form["med_name"]
        med_time = request.form["med_time"]
        email = request.form["email"]

      
        reminder_manager.add_reminder(med_name, med_time, email)
        print(f"📝 Saved Reminder: {med_name} at {med_time} for {email}")



        return redirect(
            url_for("index")
        )  
    reminders = reminder_manager.get_all_reminders()
    return render_template("index.html", reminders=reminders)



if __name__ == "__main__":
    app.run(debug=True)
