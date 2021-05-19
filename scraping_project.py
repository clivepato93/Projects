import requests
from bs4 import BeautifulSoup
from random import choice

def h():
    i=1
    response= requests.get(f"http://quotes.toscrape.com/page/{i}/")
    q=[]
    t=True
    while t:
        response= requests.get(f"http://quotes.toscrape.com/page/{i}/")
        soup = BeautifulSoup(response.text,"html.parser")
        last=soup.find(class_="next")
        if last:
            q.append(f"http://quotes.toscrape.com/page/{i}/")
            i+=1

        else:
            q.append(f"http://quotes.toscrape.com/page/{i}/")
            t=False
    return q
s=[]
for link in h():
    response=requests.get(link)
    soup= BeautifulSoup(response.text,"html.parser")
    quotes=soup.find_all(class_="quote")
    for quote in quotes:
        bio=quote.find("a")["href"]
        name=quote.find("small").get_text()
        text=quote.find(class_="text").get_text()
        s.append([text,name,bio])

c=s[-18]
r=requests.get(f"http://quotes.toscrape.com/"+(c[2]))
soup= BeautifulSoup(r.text,"html.parser")
name_details=c[1].split()
desc_b=soup.find(class_="author-born-date").get_text()
desc_p=soup.find(class_="author-born-location").get_text()

# print("The celebrity was born on",desc_b,desc_p)

hints=["Here's a hint The celebrity was born on "+desc_b+" "+desc_p
       ,f"Here's a hint the celebrity first name begins with {name_details[0][0]}"
       ,f"Here's a hint the celebrity last name begins with {name_details[-1][0]}"][::-1]

t=True
g=0

while t:
    if g==0:
        print("Who said this quote ", c[0])
    guess=input("Please enter your guess ").lower()
    if guess==c[1].lower():
        print("Congrats would you like to play again (y/n)?")
        play=input().lower()
        if play=="y":
            t=True
            g=0
        else:
            t=False
    elif guess!=c[1].lower() and hints:
        g+=1
        print(hints.pop())
    elif guess!=c[1].lower() and not hints:
        g+=1
    if g==4:
        print("The person was "+c[1])
        print("Would you like to play again (y/n)?")
        play=input().lower()
        if play=="y":
            t=True
            g=0
        else:
            t=False
