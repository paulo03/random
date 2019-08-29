from datetime import datetime
from datetime import date

def find_age(dob):
    dob = dob.split()
    # dob split = [DAY, MONTH, YEAR]
    
    month = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5,
             'JUN': 6, 'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10,
             'NOV': 11, 'DEC': 12}
    
    today = date.today()
    today = datetime.__str__(datetime.today())
    today = today[0:10]
    # today format = 'YYYY-MM-DD'
    
    year = int(today[0:4]) - int(dob[2])
    month = int(today[5:7]) - int(month[str(dob[1])])
    day = int(today[8:10]) - int(dob[0])

    if month > 0:
        return year
    elif month < 0:
        return year - 1
    else:
        if day >= 0:
            return year
        else:
            return year - 1
