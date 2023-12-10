# Rate my Babson Course
Problem solving and software design final project

Luna Dayan & Juanse Arosemena

### Project Big Idea
Our website allows Babson College students to rate courses and view arggregated course ratings. The students will be able to rate the class based on usefulness, difficulty, and workload.TThey will also have the opportunity to provide any additional comments for other students. The m#ain goal of our project is to provide a valuable resource for current and future students that will help them make a more informed decision when it comes to course registration.

### The code explained
#### Before you run the code
Before you run any code you will have to install some libraries in your computer. Those libraries are: flask, json, csv, BeautifulSoup and urllib.request. 

#### Start by scraping Babson's website 
After you have all the libraries installed, scraping the website is the next step. With the scraper.py file you are going to be able to download the entire page, and scrape the course name, course number and course level of each of Babson College courses. The information gathered will be saved in a csv file named babson_courses.csv.

#### Flask for the website
To create the website, we are going to be using Flask. In the app.py file you will see all the templates gathered and used to create the website. The templates in use are: course.html, index.html, rate_course.html and search_results.html. All of those templates are in use and each one has their own purpose in the app.py file. 

#### How the website works
When you open the website, you are going to be welcomed by a page and will be asked to enter the course number of the course you want to search. After, you will get the different options of courses with the course number that you entered. When you click the course you want, it will direct you to the ratings page, were the past ratings will be shown. The website will have a bottom for you to rate the course, if you want to rate it you can click on it. The website will ask you for 3 specific ratings (usefulness, difficulty and workload) and there is a space for extra comments. After submiting the ratings, you can return to the mane page or you can see all the ratings for the course you rated. 

#### Ratings information stored
All the ratings that users submit are going to be stored in a json file called ratings.json.
