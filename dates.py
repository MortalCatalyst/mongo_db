import datetime


base = datetime.datetime(2017,1,1)

def datesRange(max, min):
    date_list = [base - datetime.timedelta(days=x) for x in range(max,min)]
    return date_list

dateValues = datesRange(-210,0)

def dateDay(dayToCheck):
    """
    get a date from the generator
    confirm if its saturday.
    """
    mySaturdays = []
    for day in dateValues:
        if day.weekday() == dayToCheck:
            mySaturdays.append(day)
    return mySaturdays


listOfDates = dateDay(5)
print(listOfDates)
