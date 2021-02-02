import ezsheets

ss = ezsheets.Spreadsheet('1dFsi_grEKhKPFFx2EkJRVs0FRU-LV3fq1nqbmVneFIM')
print(ss.title)
# ask for password before running program
guessAttempts = 3
password = "161616"
userPassword = input("Enter 6-digit password: ")
guessAttempts -= 1

while (userPassword != password and guessAttempts >= 0):
    if (guessAttempts == 0):
        print("No more attempts. Program is closing...")
        quit()
    guessAttempts -= 1
    userPassword = input("Try again. Enter 6-digit password: ")

print("Program will now start!")


# when program runs, automatically update my infos using apis and save the info to google sheets

"""show an options menu with choices:
    1) view current total assets
        a) investments
        b) liquid assets
    2) view assets history (makes a graph)
        a) over the last week
        b) over the last month 
        c) over the last year
        d) over the last x years
        e) all time
    3) view spendings 
        a) amount spent each month
        b) amount spent each month by category
    4) view stock assets
        a) change overtime in stock assets 
        b) view stock portfolio 
"""
