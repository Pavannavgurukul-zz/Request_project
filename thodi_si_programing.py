import requests
import json
import pprint
import os 

if os.path.isfile('./courses.json'):
	file=open("courses.json")
	temp=file.read()
	data=json.loads(temp)
	file.close()
else:
	request=requests.get("http://saral.navgurukul.org/api/courses")
	data=request.json()
	s=json.dumps(data)
	with open("courses.json", "w") as file:
		file.write(s)
		file.close()

list_of_id=[]
for i in range(len(data["availableCourses"])):
	print(i+1,data["availableCourses"][i]["name"])
	list_of_id.append(data["availableCourses"][i]["id"])


choice=int(input("Which course you want to join  "))
for i in range(len(list_of_id)):
	if (choice-1)==i:
		if os.path.isfile("./exercises_"+str(list_of_id[i])+".json"):
			file=open("exercises_"+str(list_of_id[i])+".json")
			temp=file.read()
			subdata=json.loads(temp)
			file.close()
		else:
			request1=requests.get("http://saral.navgurukul.org/api/courses/"+str(list_of_id[i])+"/exercises")
			subdata=request1.json()
			s=json.dumps(subdata)
			with open("exercises_"+str(list_of_id[i])+".json", "w") as f:
				f.write(s)
				f.close()

	
parent=subdata["data"]
slugP=[]
for i in range(len(parent)):
	print(str(i+1),parent[i]["name"])
	slugP.append(parent[i]["slug"])
	for j in range(len(parent[i]['childExercises'])):
		print("\t"+str(j+1),parent[i]['childExercises'][j]["name"])
		slugP.append(parent[i]['childExercises'][j]["slug"])


user_input=int(input("Enter which slug you want to see  "))# for i in range(len(slugP)):# 	if (user_input-1)==i:# 		request2=requests.get("http://saral.navgurukul.org/api/courses/12/exercise/getBySlug?slug="+str(slugP[i]))# 		slug_1=request2.json()# 		print(slug_1["content"])
for i in range(len(slugP)):
	if (user_input-1)==i:
		if os.path.exists("./exercise_pavan_"+str(user_input)+".json"):
			file=open("exercise_pavan_"+str(user_input)+".json")
			temp=file.read()
			slug_1=json.loads(temp)
			file.close()
			print(slug_1["content"])
		else:
			request2=requests.get("http://saral.navgurukul.org/api/courses/12/exercise/getBySlug?slug="+str(slugP[i]))
			sc=request2.json()
			p=json.dumps(sc)
			with open("exercise_pavan_"+str(user_input)+".json", "w") as f:
				f.write(p)
				f.close()

			f=open("exercise_pavan_"+str(user_input)+".json")
			temp=f.read()
			slug_1=json.loads(temp)
			f.close()
			print(slug_1["content"])