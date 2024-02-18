import requests
import json
from datetime import datetime

# Fetch random numbers from API
response = requests.get("https://www.random.org/sequences/?min=1&max=100&format=plain&rnd=new&col=4")
random_numbers = [list(map(int, line.split())) for line in response.text.strip().split('\n')]
#print(random_numbers)

categories = ["performance", "entrepreneurship", "authenticity", "kindness"]
#print(categories)

data = []

for row in random_numbers:
    count=0
    row_data = {}
    for element in row:
        #print(element, end=' ')
        if element >= 90:
            grade = "peaker"
            suggestion = "keep up the great work peaker"
        else:
            grade = "not yet peaker"
            suggestion = "work on improving to reach peaker status"
        category=categories[count%4]
        count+=1
        row_data[category] = {
            "percentage": element,
            "grade": grade,
            "suggestion": suggestion
        }
        #print(grade,suggestion,category)
    data.append(row_data)
    #print()

json_data = json.dumps(data, indent=4)

print(json_data)

current_date = datetime.now().strftime("%Y-%m-%d")
file_name = f"grader_output_{current_date}.json"

with open(file_name, "w") as json_file:
    json_file.write(json_data)