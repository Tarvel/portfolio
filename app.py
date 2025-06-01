from flask import Flask, render_template, send_file, request
import json, os
from send_email import notify_mail

app = Flask(__name__)


@app.route('/')
def index():
    page ='home'
    
    return render_template('index.html', page=page, title='Home | Tai')

@app.route('/projects')
def projects():
    page ='projects'
    with open('projects.json', 'r') as json_data:
        projects = json.load(json_data)
    return render_template('projects.html', projects=projects, page=page, title='Projects | Tai')

@app.route('/about')
def about():
    page = 'about'

    return render_template('about.html', page=page)

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    page = 'contact'

    if request.method == 'POST':
        name = request.form.get('name', 'default_value')
        email = request.form.get('email', 'default_value')
        message = request.form.get('message', 'default_value')

        text = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        notify_mail(text)

    return render_template('contact.html', page=page)

@app.route('/my_resume')
def download_file():
    path = "static/Taiye_s_Resume.pdf"
    return send_file(path, as_attachment=True, download_name="Taiye_s_Resume.pdf")



if __name__ == '__main__':
    app.run(debug=True)
