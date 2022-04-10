from itertools import product
import json
import requests
from bs4 import BeautifulSoup

def extract_element(ancestor, selector):
    try:
        return ancestor.select(selector).pop(0).text.strip()
    except: return None
product_id = input("Podaj identyfikator produktu: ")
url_pre = "https://www.ceneo.pl"
url_post = "/opinie-"
page_no = 1

all_reviews = []


while(page_no):
    url = url_pre+product_id+url_post+str(page_no)
    response= requests.get(url, allow_redirects=False)
        if  response.status_code == requests.codes.ok:
        page_dom = BeautifulSoup(response.text, 'html.parser')
        reviews = page_dom.select("div.js_product-review")
        for review in reviews:
            review_id = review["data-entry-id"]
            author = review.select("span.user-post__author-name").pop(0).text.strip()
            try:
                recommendation = review.select("span.user-post__author-recomendation > em").pop(0).text
                recommendation = True if recommendation == "Polecam" else False
            except: recommendation == None
            stars = review.select("span.user-post__score-count").pop(0).text
            stars = float(stars.split("/").pop(0).replace(",","."))
            content = review.select("div.user-post__text").pop(0).get_text()
            content = content.replace("\n"," ").replace("  "," ").strip()
            publish_date = review.select("span.user-post__published > time:nth-child(1)").pop(0)["datetime"]
            publish_date = publish_date.split(" ").pop(0)
            try:
                purchase_date = review.select("span.user-post__published > time:nth-child(1)").pop(0)["datetime"]
                purchase_date = purchase_date.split(" ").pop(0)
            except IndexError: purchase_date = None
            useful = review.select("button.vote-yes >span").pop(0).text
            useful = int(useful)
            useless = review.select("button.vote-no >span").pop(0).text
            useless = int(useless)
            pros = review.select("div.review-feature__title--positives ~ div.review-feature__item")
            pros = [item.text.strip() for item in pros]
            pros = ", ".join(pros)
            cons = review.select("div.review-feature__title--positives ~ div.review-feature__item")
            cons = [item.text.strip() for item in cons]
            cons = ", ".join(cons)
            single_review = {
                "review_id": review_id,
                "author": author,
                "recommendation": recommendation,
                "stars": stars,
                "content": content,
                "publish_date": publish_date,
                "purchase_date": purchase_date,
                "useful": useful,
                "useless": useless,
                "pros": pros,
                "cons": cons
            }

            all_reviews.append(single_review)
        page_no+=1
    else: page_no = None

f = open("reviews/"+product_id+".json","w", encoding="UTF-8")
json.dump(all_reviews,f, indent=4, ensure_ascii=False)
