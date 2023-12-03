from flask import Flask, render_template, request, flash, url_for, redirect
import csv

app = Flask(__name__)

@app.route('/')
def get_course_name():
    with open('data/babson_courses.csv') as f:
        data = csv.reader(f, delimiter = ",")
        first_line = True
        courses = []
        for row in data:
            if not first_line:
                courses.append({
                    "name": row[0],
                    "course_number": row[1],
                    "course_level": row[2]
                })
            else:
                first_line = False
    return render_template("index.html", courses = courses)



@app.route(f'/{course_search}')
def courses_search():
    return render_template("course")

if __name__=="__main__":
    app.run(debug=True)
