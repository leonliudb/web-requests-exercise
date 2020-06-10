print("REQUESTING SOME DATA FROM THE INTERNET...")

import json
import requests
import statistics
print("----------")
print("PART 1")
product_response = requests.get("https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json")
product = json.loads(product_response.text)
print(product["name"])
print("----------")
print("PART 2")
products_response = requests.get("https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json")
products = json.loads(products_response.text)
for p in products:
    print(f" {p['id']} {p['name']}")
print("----------")
print("PART 3")
gradebook_response = requests.get("https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json")
gradebook = json.loads(gradebook_response.text)
#print(gradebook)
#breakpoint()
grades = [s["finalGrade"] for s in gradebook["students"]]
print("MIN:", min(grades))
print("MAX:", max(grades))
print("AVG:", statistics.mean(grades))