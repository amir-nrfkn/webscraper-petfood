from bs4 import BeautifulSoup
import requests

# Web Scraper for pet food (Fromm)

url = input("Enter link: ")
response = requests.get(url)
page = response.text
soup = BeautifulSoup(page, "html.parser")

special_char = {
	"À":"A",
	"á":"a",
	"â":"a",
	"é":"e",
	"®":"",
	"[":"",
	"]":"",
	"¬":"",
	"†":"",
	"™":"",
	"Ñ":"",
	"¢":""
}

# NAME
name = soup.find(name="span", class_="title").getText()
for a, b in special_char.items():
	name = name.replace(a, b)
print(name)

# DESCRIPTION
description = soup.find('div', {"class": "content col-sm-8"}).p.getText()
for a, b in special_char.items():
	description = description.replace(a, b)
# print(description)

# IMAGE
image = soup.find('div', {"class": "image col-sm-4"}).img.get('src')
# print(image)

# INGREDIENTS
all_ingredients = soup.find('div', {"class": "ingredients col-sm-7"}).p.find_all("a")
ingredients = str([i.getText().replace(",", "") for i in all_ingredients]).replace("'", "")
for a, b in special_char.items():
	ingredients = ingredients.replace(a, b)
# print(ingredients)

# CALORIC CONTENT
calories = str(soup.find('div', {"class": "calories"}).ul).replace("\n", "")
for a, b in special_char.items():
	calories = calories.replace(a, b)
# print(calories)

# ANALYSIS
analysis = str(soup.find('div', {"class": "guaranteed col-sm-5"}).ul).replace("\n", "")
for a, b in special_char.items():
	analysis = analysis.replace(a, b)
# print(analysis)

# ALL DATA IN ARRAY
data = [name, description, image, ingredients, calories, analysis]
# print(data)

with open(f"{name}.txt", mode="w") as file:
	for i in data:
		file.write(f'''{i}"''')