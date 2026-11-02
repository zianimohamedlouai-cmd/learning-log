import json

data = [{"activity" : "Python" , "minutes" : 45}]

with open ("session.json" , "w") as f : 
    json.dump(data , f)

with open("session.json" , "r") as f : 
    loaded = json.load(f)

print(loaded)
print(type(loaded))
print(loaded[0]['minutes'] + 1)


#my prediction of the output 
#[{'activity':'Python' ,'minutes':45}]
#<class -list>
#46