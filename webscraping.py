import requests
from bs4 import BeautifulSoup

source = requests.get("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books").text
soup = BeautifulSoup(source, "lxml")

# Prints Top 50 Amazon Best Sellers in Books
for i in range(len(soup.find_all("div", class_="a-section a-spacing-none aok-relative"))):
    # Prints the name of the book
    print(i + 1, ".",
          soup.find("div", id="zg-center-div").find_all("div", class_="a-section a-spacing-none aok-relative")[i]
              .find("span", class_="aok-inline-block zg-item").find("a", class_="a-link-normal").find_all("div")[1]
              .text.strip())
    # Prints the name of the author
    print(soup.find_all("span", class_="aok-inline-block zg-item")[i].find("div", class_="a-row a-size-small").text)

    # Prints the rating of the book
    try:
        print(soup.find_all("span", class_="aok-inline-block zg-item")[i].find("div", class_="a-icon-row a-spacing-none").a["title"])
    except AttributeError:
        print("No rating")

    # Type of the book
    print(soup.find_all("span", class_="aok-inline-block zg-item")[i].find_all("div", class_="a-row a-size-small")[1].text)

    # Prints the price of the book
    print(soup.find_all("span", class_="aok-inline-block zg-item")[i].find_all("div", class_="a-row")[2].text)
    print()
