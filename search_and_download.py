#! /usr/bin/python3
import requests
from bs4 import BeautifulSoup

def download():
    """ Download the keyword images from web and store it in working directory
        where program is running """

    search_query = input("Enter image name: ")

    #google image search concatinating with search_query to search web
    url = "https://www.google.co.in/search?hl=en&tbm=isch&source=hp&biw=1296&bih=630&ei=FhcPXfXhPIbavgTYl6K4Aw&q="+\
        search_query.replace(" ","+")+"&oq="+search_query.replace(" ", "+") 
    try:
        req = requests.get(url) #getting result by http get request method
        try:
            soup = BeautifulSoup(req.text, "html.parser")
            images = soup.find_all("img") #searching img tag from html parsed object
            count = 0
            for image in images:
                resp = requests.get(image['src']) #get the src address of listed images
                with open(search_query+str(count)+".jpeg", "wb") as f:    #save byte form as search_query+count+extension(.jpeg) 
                    f.write(resp.content)
                    count += 1
            print("Images downloaded Successfully")
        except Exception as e:
            print(e)
    except Exception as e:
        print("Check internet connection or it may be request error")
 
download()
