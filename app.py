from flask import Flask, render_template, request, flash, url_for, redirect, Blueprint
import csv

app = Flask(__name__)

CSV_FILE = "data/babson_courses.csv"
data = []
with open(CSV_FILE) as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)

@app.route('/')
def index():
    return render_template("index2.html")


@app.route("/search")
def search():
    query = request.args.get("q")
    matched_data = []
    for row in data:
        if query.lower() in row[1].lower():
            matched_data.append(row)
    return jsonfy(matched_data)

    # return render_template("index.html")


#     print(q)

#     if q:
#         f.query.filter(f.course_number.icontains(q)).order_by(f.name.desc()).limit(100).all()
#     else:
#         results = []
    
#     return render_template("search_results.html", results = results)

# @app.route(f'/{course_search}')
# def courses_search():
#     return render_template("course")

if __name__=="__main__":
    app.run(debug=True)
