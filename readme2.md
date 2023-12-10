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
