from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/projects')
def projects():
    
    return render_template('projects.html')

@app.route('/download')
def download_file():
    path = "static/Taiye_s_Resume.pdf"
    return send_file(path, as_attachment=True, download_name="Taiye_s_Resume.pdf")



if __name__ == '__main__':
    app.run(debug=True)
