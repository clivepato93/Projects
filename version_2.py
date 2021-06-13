import requests
from bs4 import BeautifulSoup
from random import choice
from random import shuffle
base = "http://quotes.toscrape.com"

def scrape():
    url = "/page/1/"
    lst = []
    while url:
        response = requests.get(base+url)
        soup = BeautifulSoup(response.text,"html.parser")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
                bio = quote.find("a")["href"]
                name = quote.find("small").get_text()
                text = quote.find(class_="text").get_text()
                lst.append({"quote":text,"name":name,"bio":bio})
        if soup.find(class_="next"):
            n = soup.find(class_="next").find("a")["href"]
        else:
            n = None
        url=n
    return lst

quoters=scrape()


def choose():
    shuffle(quoters)
    choosen_person=(choice(quoters))
    r = requests.get(f"http://quotes.toscrape.com/"+choosen_person["bio"])
    name={"first":choosen_person["name"].split()[0],"last":choosen_person["name"].split()[1]}
    s = BeautifulSoup(r.text, "html.parser")
    hints=[f"Here's is a hint the celebrity first name begins with {name['first'][:1]}",
           f"Here's a hint the celebrity last name begins with {name['last'][:1]}",
           f"Here's a hint The celebrity was born on "+"{} {}".format(*[info.get_text() for info in s.find_all("span")[:2]]),
           "Here's a hint "+s.find(class_="author-description").get_text().replace(name["first"],"").replace(name["last"],"").replace(name["first"].upper(),"").replace(name["last"].lower(),""),
           True]
    return choosen_person, hints

def play():
    # n=0
    person,hints=choose()
    print("Who said this quote ", person["quote"])
    while hints:
        guess=input("Please enter your guess ").lower()
        if guess==person["name"].lower():
            print("Congrats")
            hints=False
        elif guess!=person["name"].lower() and hints[0]!=True:
            print(hints.pop(0))
        elif hints[0]==True:
            print("The person was "+person["name"])
            hints=False

def play_again():
    g=True
    while g:
        print("Would you like to play again (y/n)?")
        i=input().lower()
        if i=="y":
            play()
        elif i=="n":
            g=False
        else:
            print("Would you like to play again (y/n)?")
            i=input().lower()

play()
play_again()
