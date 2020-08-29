from datetime import time, tzinfo, timedelta, datetime

class Date:

    def __init__(self):
        {}


    def getDate(self):
        return datetime.today().strftime('%d/%m/%y')

    def getDay(self):
        day = datetime.today().strftime('%A')
        if day == "Monday":
            day = "Lundi"
        elif day == "Tuesday":
            day = "Mardi"
        elif day == "Wednesday":
            day = "Mercredi"
        elif day == "Thursday":
            day = "Jeudi"
        elif day == "Friday":
            day = "Vendredi"
        elif day == "Saturday":
            day = "Samedi"
        else:
            day = "Dimanche"
        return day

