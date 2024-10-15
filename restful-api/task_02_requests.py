#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()


        for post in posts:
            print (post['title'])

    else:
        print("la requête a échoué.")

def fetch_and_save_posts():
    # Effectuer la requête pour récupérer les posts
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Vérifier si la requête est réussie
    if response.status_code == 200:
        # Parser les données JSON
        posts = response.json()

        posts_list = [{'id': post['id'], 'title': post['title'], 'body': post['body']}
                     for post in posts]

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts_list)
        print("Posts have been save")
    else:
        print("La requête a échoué.")
