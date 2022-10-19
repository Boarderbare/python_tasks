import datetime
from time import strptime
from xmlrpc.client import DateTime

month = int(input("Input month of your birthday  "))
day = int(input("Input day of your birthday  "))
year = datetime.date.today().year
yearS = yearE =year;

birthday = datetime.datetime(year, month, day)
zodiacs = {
    "Aries": ("21 March", "20 April"),
    "Taurus": ("21 April", "21 May"),
    "Cancer": ("22 June", "22 July"),
    "Gemini": ("22 May", "21 June"),
    "Leo": ("23 July", "21 August"),
    "Virgo": ("22 August", "23 September"),
    "Libra": ("24 September", "23 October"),
    "Scorpio": ("24 October", "22 November"),
    "Sagittarius": ("23 November", "22 December"),
    "Aquarius": ("21 January", "19 February"),
    "Pisces": ("20 February", "20 March"),
    "Capricorn": ("23 December", "20 January"),
}

for key, value in zodiacs.items():
    start = value[0]
    end = value[1]

    if (month == 1 and day <= 20 and key=="Capricorn"):
        yearS -= 1

    if (month == 12 and day >= 23 and key=="Capricorn"):
        yearE += 1

    dateStart = datetime.datetime.strptime(str(yearS) + " " + start, "%Y %d %B")
    dateEnd = datetime.datetime.strptime(str(yearE) + " " + end, "%Y %d %B")

    if (dateStart < birthday < dateEnd):
        print("Your sign is  " + key)

input("Press Enter to continue...")

