import requests
from bs4 import BeautifulSoup
import csv
from random import choice

# with open("quotes_data.csv", "w") as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["quote", "person", "bio-link"])

def scrape():
    base = "http://quotes.toscrape.com"
    url = "/page/1/"
    lst = []
    while url:
        response = requests.get(base+url)
        soup = BeautifulSoup(response.text,"html.parser")
        quotes = soup.find_all(class_="quote")
        # with open("quotes_data.csv", "a") as csv_file:
        #     writer = csv.writer(csv_file)
        for quote in quotes:
                bio = quote.find("a")["href"]
                name = quote.find("small").get_text()
                text = quote.find(class_="text").get_text()
                lst.append([text, name, bio])
                # writer.writerow([text, name, bio])
        if soup.find(class_="next"):
            n = soup.find(class_="next").find("a")["href"]
        else:
            n = None
        url = n
    c=choice(lst)
    # print(c)
    r=requests.get(f"http://quotes.toscrape.com/"+(c[2]))
    s= BeautifulSoup(r.text,"html.parser")
    name_details=c[1].split()
    desc_b=s.find(class_="author-born-date").get_text()
    desc_p=s.find(class_="author-born-location").get_text()
    # soup= BeautifulSoup(r.text,"html.parser")
    name_details=c[1].split()

    hints=["Here's a hint The celebrity was born on "+desc_b+" "+desc_p
       ,f"Here's a hint the celebrity first name begins with {name_details[0][0]}"
       ,f"Here's a hint the celebrity last name begins with {name_details[1][0]}"][::-1]
    t=True
    g=0

    while t:
        if g==0:
            print("Who said this quote ", c[0])
        guess=input("Please enter your guess ").lower()
        if guess==c[1].lower():
            print("Congrats would you like to play again (y/n)?")
            play=input().lower()
            x=True
            while x:
                if play=="y":
                    # t=True
                    g=0
                    c=choice(lst)
                    # print(c)
                    r=requests.get(f"http://quotes.toscrape.com/"+(c[2]))
                    s= BeautifulSoup(r.text,"html.parser")
                    name_details=c[1].split()
                    desc_b=s.find(class_="author-born-date").get_text()
                    desc_p=s.find(class_="author-born-location").get_text()
                    # soup= BeautifulSoup(r.text,"html.parser")
                    name_details=c[1].split()

                    hints=["Here's a hint The celebrity was born on "+desc_b+" "+desc_p
                    ,f"Here's a hint the celebrity first name begins with {name_details[0][0]}"
                    ,f"Here's a hint the celebrity last name begins with {name_details[1][0]}"][::-1]
                    t=True
                    # g=0
                    x=False
                elif play=="n":
                    x=False
                    t=False
                else:
                    print("Congrats would you like to play again (y/n)?")
                    play=input().lower()
        elif guess!=c[1].lower() and hints:
            g+=1
            print(hints.pop())
        elif guess!=c[1].lower() and not hints:
            g+=1
        if g==4:
            print("The person was "+c[1])
            print("Would you like to play again (y/n)?")
            play=input().lower()
            x=True
            while x:
                if play=="y":
                # t=True
                    g=0
                    c=choice(lst)
                # print(c)
                    r=requests.get(f"http://quotes.toscrape.com/"+(c[2]))
                    s= BeautifulSoup(r.text,"html.parser")
                    name_details=c[1].split()
                    desc_b=s.find(class_="author-born-date").get_text()
                    desc_p=s.find(class_="author-born-location").get_text()
                # soup= BeautifulSoup(r.text,"html.parser")
                    name_details=c[1].split()

                    hints=["Here's a hint The celebrity was born on "+desc_b+" "+desc_p
                ,f"Here's a hint the celebrity first name begins with {name_details[0][0]}"
                ,f"Here's a hint the celebrity last name begins with {name_details[1][0]}"][::-1]
                    t=True
                # g=0
                    x=False
                elif play=="n":
                    x=False
                    t=False
                else:
                    print("Would you like to play again (y/n)?")
                    play=input().lower()
scrape()
