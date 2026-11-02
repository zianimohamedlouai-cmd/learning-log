sessions =[]
sessions.append({"activity" : "Python" , "minutes" : 45 })
sessions.append({"activity" : "Gym" , "minutes" : 60 })
print(sessions)
print(sessions[0])
print(sessions[1]["activity"])
for s in sessions:
    print(s["activity"], s["minutes"])
