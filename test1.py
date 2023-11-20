import csv
import urllib.request
from bs4 import BeautifulSoup 


DOWNLOAD_URL = "https://www.babson.edu/about/course-catalog/new-course-search/?courseType=undergraduate"


def download_page(url):
    """
    Download the entire page given an URL
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    request = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(request)

# print(download_page(DOWNLOAD_URL).read())

def parse_html(html):
    soup = BeautifulSoup(html, features='html.parser')

    course_list = soup.find("div", attrs={"id": "section-content"})
    courses = []
    for row in course_list.find_all("div", attrs={"class":"course-listing"}):

        #print name
        name = row.find("div", attrs={"class":"h3"})
        print(name)

        #print course level 
        course_number = row.find("span", attrs={"data-catname": "courseCode"})
        print(course_number)

        courses.append((name, course_number))

    return courses

parse_html(download_page(DOWNLOAD_URL).read())

def main():
    url = DOWNLOAD_URL

    with open("data/babson_courses.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)

        fields = ("name", "course_number")
        writer.writerow(fields)

        html = download_page(url)
        courses = parse_html(html)
        writer.writerows(courses)


if __name__ == "__main__":
    main()


    


