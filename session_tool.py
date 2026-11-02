def ask_session():
    session ={}
    session['activity'] = input ('Activity : ')
    session['minutes'] = int(input ('minutes  : '))
    return(session)
data = ask_session()
print(data["minutes"] + 1)