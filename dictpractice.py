
session = {"activity" : "python" , "minutes" : 45 }
print(session["activity"])
session ["minutes"] = 60
session ["done"] = True
print (session)

session["activity"] = input("Activity : ")
print(session["activity"])
session["minutes"] = int(input("minutes : "))
print(f'{session["activity"]}  {session["minutes] }')