import matplotlib.pyplot as p
import numpy as np
import requests
from datetime import date
import schedule
import time


def plotGraph():

    daysFile = open("days.txt", "r")
    infectedFile = open("infected.txt", "r")

    daysLines = daysFile.readlines()
    infectedLines = infectedFile.readlines()

    days = []
    infected = []

    for line in daysLines:
        days.append(line.rstrip("\n"))

    for line in infectedLines:
        infected.append(int(line))

    p.plot(days, infected)
    p.xlabel('Date')
    p.ylabel('Total Infected')
    p.title('COVID-19 cases in Santa Clara County')

    p.xticks(np.arange(0, len(days), step=14))
    p.show()

def getCases():
    r = requests.get("https://www.sccgov.org/sites/phd/DiseaseInformation/novel-coronavirus/Pages/home.aspx")
    sourceCode = r.text
    index = sourceCode.find("Total_Confirmed_Cases")
    cases = int(sourceCode[index+24:index+27]) #Gets the cases number from the html code
    return cases

def addCasesToFile(cases):
    today = str(date.today())
    today = today[6:] #Strips the year away from date format

    daysFile = open("days.txt", "a")
    infectedFile = open("infected.txt", "a")

    daysFile.write(today+"\n")
    infectedFile.write(str(cases))

    daysFile.close()
    infectedFile.close()

def executeEverything():
    print("running executeEverything()")
    cases = getCases()
    addCasesToFile(cases)
    plotGraph()

if __name__ == '__main__':
    schedule.every().day.at("03:00").do(executeEverything)
    while True:
        schedule.run_pending()
        time.sleep(60) # wait one minute