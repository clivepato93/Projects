from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
from random import choice


def getlinks():
    q=[]
    i=0
    url=f"http://quotes.toscrape.com/page/{i}/"
    for i in range(1,11):
        q.append(f"http://quotes.toscrape.com/page/{i}/")
    return q

def exact_info():
    s=[]
    link_picker=choice(getlinks())
    response=requests.get(link_picker)
    soup= BeautifulSoup(response.text,"html.parser")
    quotes=soup.find_all(class_="quote")
    for quote in quotes:
        bio=quote.find("a")["href"]
        name=quote.find("small").get_text()
        text=quote.find(class_="text").get_text()
        s.append([text,name,bio])

    c=choice(s)
    r=requests.get(f"http://quotes.toscrape.com/"+(c[2]))
    soup= BeautifulSoup(r.text,"html.parser")
    name_details=c[1].split()
    desc_b=soup.find(class_="author-born-date").get_text()
    desc_p=soup.find(class_="author-born-location").get_text()
    return c,name_details,desc_b,desc_p

def play():
    hints=["Here's a hint The celebrity was born on "+exact_info()[-2]+" "+exact_info()[-1]
       ,f"Here's a hint the celebrity first name begins with {exact_info()[1][0][0]}"
       ,f"Here's a hint the celebrity last name begins with {exact_info()[1][1][0]}"][::-1]


    t=True
    g=0

    while t:
        if g==0:
            print("Who said this quote ", exact_info()[0][0])
        guess=input("Please enter your guess ").lower()
        if guess==exact_info()[0][1].lower():
            print("Congrats would you like to play again (y/n)?")
            play=input().lower()
            if play=="y":
                t=True
                g=0
            else:
                t=False
        elif guess!=exact_info()[0][1].lower() and hints:
            g+=1
            print(hints.pop())
        elif guess!=exact_info()[0][1].lower() and not hints:
            g+=1
        if g==4:
            print("The person was "+exact_info()[0][1])
            print("Would you like to play again (y/n)?")
            play=input().lower()
            if play=="y":
                t=True
                g=0
            else:
                t=False

play()
