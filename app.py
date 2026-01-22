from flask import Flask, render_template, send_file, request, jsonify
import json
from send_email import notify_mail

app = Flask(__name__)


@app.route("/")
def index():
    page = "home"
    
    # Load projects data
    with open("projects.json", "r") as json_data:
        projects = json.load(json_data)
    
    return render_template("index.html", page=page, title="Home | Tai", projects=projects)


@app.route("/projects")
def projects():
    return index()


@app.route("/about")
def about():
    return index()


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form.get("namke", "default_value")
        email = request.form.get("email", "default_value")
        message = request.form.get("message", "default_value")

        text = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        notify_mail(text)
        
        return jsonify({"success": True, "message": "Message sent successfully!"})

    return index()


@app.route("/my_resume")
def download_file():
    path = "static/Taiye_s_CV.pdf"
    return send_file(path, as_attachment=True, download_name="Taiye_s_CV.pdf")


if __name__ == "__main__":
    app.run(debug=True)
