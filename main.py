from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


@app.route("/") #pfad
def index():
    welcometext = "Herzlich Willkommen"
    currentyear = datetime.datetime.now().year
    vemap=["Martin", "Hani", "Anna", "Markus"]
    return render_template("index.html", welcometext=welcometext, currentyear=currentyear, vemap=vemap)


@app.route("/about-me")
def about():
    return render_template("about.html")


@app.route("/help-me")
def help():
    return render_template("help.html")


@app.route("/contact", methods=["POST"])
def contact():
    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_message = request.form.get("contact-message")
    print(contact_name)
    print(contact_email)
    print(contact_message)
    return render_template("success.html")


if __name__ == '__main__':
    app.run()
