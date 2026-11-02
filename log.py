def ask_session():
    activity = input("Activity (q to quit): ")
    if activity == "q":
        return None
    minutes = int(input("Minutes : "))
    return {'activity' : activity , 'minutes': minutes}

sessions = []
session = ask_session()
while session is not None:
    sessions.append(session)
    session = ask_session()
def summarize(sessions):
    total = 0
    for s in sessions:
       print(s)
       total += s["minutes"]
    total_hours = round(total / 60 , 1)
    print (f'The total hours is {total_hours}')

summarize(sessions)