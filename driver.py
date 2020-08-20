import requests
import re

if __name__ == '__main__':
    dept = input("Enter code for the department offering the class (ex: MATH, CMSC): ")
    number = input("Enter the class number (ex: 216, 101): ")
    class_name = dept + number

    url = "http://app.testudo.umd.edu/soc/search?courseId=" + class_name + "&sectionId=&termId=202008&_openSectionsOnly=on&creditCompare=&credits=&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on"
    r = requests.get(url)
    code = r.text

    indeces = [m.start() for m in re.finditer('open-seats-count">', code)]
    htmlLen = len('open-seats-count">')
    openSeats = []

    for i in indeces:
        openSeats.append(code[i + htmlLen : i + htmlLen + 2])

    openSeats = [int(s.replace('<', '')) for s in openSeats]
    print(sum(openSeats))

