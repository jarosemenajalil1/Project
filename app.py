from flask import Flask, render_template, request, redirect, url_for
import csv
import json

app = Flask(__name__)

CSV_FILE = "data/babson_courses.csv"
data = []
with open(CSV_FILE) as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)

def store_rating(course_number, usefulness, difficulty, workload, comment):
    # Load existing data
    try:
        with open('ratings.json', 'r') as file:
            ratings = json.load(file)
    except FileNotFoundError:
        ratings = {}

    # Update with new rating
    if course_number not in ratings:
        ratings[course_number] = []
    ratings[course_number].append({
        "usefulness": usefulness,
        "difficulty": difficulty,
        "workload": workload,
        "comment": comment
    })

    # Save data back to file
    with open('ratings.json', 'w') as file:
        json.dump(ratings, file)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("q")
    matched_data = []
    for row in data:
        if query.lower() in row[1].lower():
            matched_data.append(row)
    return render_template("search_results.html", results=matched_data)

@app.route("/rate_course/<course_number>", methods=["GET", "POST"])
def rate_course(course_number):
    if request.method == "POST":
        usefulness = request.form.get("usefulness")
        difficulty = request.form.get("difficulty")
        workload = request.form.get("workload")
        comment = request.form.get("comment")

        # Store the rating
        store_rating(course_number, usefulness, difficulty, workload, comment)

        # Redirect to the course details page
        return redirect(url_for("course", course_number=course_number))

    return render_template("rate_course.html", course_number=course_number)


@app.route("/course/<course_number>")
def course(course_number):
    # Load ratings from JSON
    try:
        with open('ratings.json', 'r') as file:
            all_ratings = json.load(file)
    except FileNotFoundError:
        all_ratings = {}

    course_ratings = all_ratings.get(course_number, [])

    # Fetch course details from your data (if available)
    # ...

    return render_template("course.html", course_number=course_number, ratings=course_ratings)

@app.route("/average_ratings")
def show_average_ratings():
    average_ratings = calculate_average_ratings()
    return render_template("average_ratings.html", average_ratings=average_ratings)

if __name__ == "__main__":
    app.run(debug=True)
