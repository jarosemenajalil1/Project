from flask import Flask, render_template, request, flash, url_for, redirect

app = Flask(__name__)

@app.route('/')
def get_course_name():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
    