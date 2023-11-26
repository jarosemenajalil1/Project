import csv
import urllib.request
from bs4 import BeautifulSoup


FIRST_PAGE = "https://www.babson.edu/about/course-catalog/new-course-search/?courseType=undergraduate&page=1"


def download_page(url):
    """
    Download the entire page given an URL
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    request = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(request)


# print(download_page(FIRST_PAGE).read())


def parse_html(html):
    """
    Scrape one Babson course search webpage
    """
    soup = BeautifulSoup(html, features="html.parser")

    course_list = soup.find("div", attrs={"id": "section-content"})
    courses = []
    for row in course_list.find_all("div", attrs={"class": "course-listing"}):
        # print name
        name = row.find("div", attrs={"class": "h3"}).get_text().strip()
        print(name)

        # print course level
        course_number = (
            row.find("span", attrs={"data-catname": "courseCode"}).get_text().strip()
        )
        print(course_number)

        # Get course level
        course_level_span = row.find("span", attrs={"data-catname": "courseLevel"})
        if course_level_span is not None:
            course_level = course_level_span.get_text().strip()
        else:
            course_level = "N/A"
        print(course_level)

        courses.append((name, course_number, course_level))
    return courses


# parse_html(download_page(FIRST_PAGE).read())


def scrape_all_pages():
    """Scrape all pages (1-45) and return a list of all courses"""
    all_courses = []

    for x in range(1, 46):
        url = f"https://www.babson.edu/about/course-catalog/new-course-search/?courseType=undergraduate&page={x}"
        html = download_page(url)
        courses_on_page = parse_html(html)
        all_courses.extend(courses_on_page)

    return all_courses


def write_data_to_csv(courses: list):
    with open("data/babson_courses.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)

        fields = ("name", "course_number", "course_level")
        writer.writerow(fields)

        writer.writerows(courses)


def main():
    """"""
    courses = scrape_all_pages()
    write_data_to_csv(courses)


if __name__ == "__main__":
    main()