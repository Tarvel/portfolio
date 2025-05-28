from flask import Flask, render_template, send_file
import json, os

app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/projects')
def projects():
    with open('projects.json', 'r') as json_data:
        projects = json.load(json_data)
    return render_template('projects.html', projects=projects)

@app.route('/my_resume')
def download_file():
    path = "static/Taiye_s_Resume.pdf"
    return send_file(path, as_attachment=True, download_name="Taiye_s_Resume.pdf")



if __name__ == '__main__':
    app.run(debug=False)
