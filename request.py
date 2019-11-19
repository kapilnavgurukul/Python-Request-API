import requests
import json
from os import path
from pprint import pprint
if path.exists("courses.json"):
    with open("courses.json","r") as file:
        data1=json.load(file)
        data=json.loads(data1)
        file.close
else:
    url="http://saral.navgurukul.org/api/courses"
    a=requests.get(url)
    with open('courses.json',"w") as file:
        b=json.dump(a.text,file)
    with open("courses.json","r") as file:
        data1=json.load(file)
        data=json.loads(data1)
        file.close

a=1
for i in data["availableCourses"]:
    print (a,"  ",i["name"])
    a+=1

user=int(input("give any number \n"))
id_=(data["availableCourses"][user-1]["id"])
print("\n")

if path.exists("exercises_"+str(id_)+".json"):
    with open("exercises_"+str(id_)+".json","r") as new_file:
        new_data1=json.load(new_file)
        new_data=json.loads(new_data1)
        new_file.close
else:
    new_data_url=requests.get("http://saral.navgurukul.org/api/courses/"+str(id_)+"/exercises")
    print(new_data_url.text)
    with open("exercises_"+str(id_)+".json","w") as new_file:
        z=json.dump(new_data_url.text,new_file)
        new_file.close
    with open("exercises_"+str(id_)+".json","r") as new_file:
        new_data1=json.load(new_file)
        new_data=json.loads(new_data1)
        new_file.close
        
a=1
for j in new_data["data"]:
    print(a,".")
    print(j["name"])
    print("          " ,j["childExercises"])
    print(j["parentExerciseId"])
    print(" ")
    a+=1

user=int(input("give input for slug"))
slug=(new_data["data"][user-1]["slug"])
print(slug)

slug_id_url="http://saral.navgurukul.org/api/courses/"+str(id_)+"75/exercise/getBySlug?slug="+slug
slug_id_data=requests.get(slug_id_url)
print(slug_id_data.text)
