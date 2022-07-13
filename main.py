
from bs4 import BeautifulSoup

import requests

import csv

import mysql.connector

# import numpy as np

URL = "https://stackoverflow.com/questions"

PAGE_LIMIT = 4

def build_url(base_url=URL, tab="newest", page=4):

    return f"{base_url}?tab={tab}&page={page}"

def scrape_page(page=1):
    response = requests.get(build_url(page=page))

    page_questions = []

    soup = BeautifulSoup(response.text, "html.parser")

    question_summary = soup.find_all(

    "h3", class_="s-post-summary--content-title")

    for summary in question_summary:

        question = summary.find("a", class_="s-link").text

        page_questions.append({
            "question": question
        })

    return page_questions
    
def scrape():

    questions = []

    page_questions = scrape_page(2)

    questions.extend(page_questions)

    return questions

mydb = mysql.connector.connect(

    host="localhost",

    user="hao",

    password="123456",

    database="mydatabase",

    auth_plugin="my_validate_password"

)

mycursor = mydb.cursor()


mycursor.execute( "USE mydatabase")

sql = "INSERT INTO questions VALUES (%s)"

val = [('haha'),

('hihi'),

('huhu'), ]

data = scrape()

for i in data:
    mycursor.execute(sql, (i["question"],))

    mydb.commit()

# if __name__ == "__main__":

#     from pprint import pprint

#     pprint(scrape())

#     export_data()

