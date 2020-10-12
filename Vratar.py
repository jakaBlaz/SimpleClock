from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
import csv

def main():
    odmor = []
    print("Delati si začel: " + str(datetime.today()))
    dan = datetime.strftime(datetime.today(),"%d.%m.%Y,%A,%X")
    print("Kakšna opomba za to merjenje časa?")
    opomba = input("1 za programiranje, 2 za prosti čas, drugače pa kr napiš kar hočeš: \n")
    try:
        opomba = opomba
        if opomba.strip() == "1":
            opomba = "Programiranje"
        elif opomba.strip() == "2":
            opomba = "Zabušavanje"
        else:
            opomba = str(opomba)
    except Exception as f:
        print(f)
    konec = 0
    while konec != 1:
        print("si že končal? 0 za premor, 1 za konec")
        konec = input()
        try:
            konec = int(konec.strip())
            if konec == 0:
                odmor = premor(odmor)
            elif konec == 1:
                break
        except:
            print("prosim vpiši številko, hvala")
            continue
    return 0

def writeTimecsv(cas):
    temporary = []
    with open('casi.csv','r', newline='') as csvfile:
        spamreader = csv.reader(csvfile,delimiter = ",",)
        i= 0
        for row in spamreader:
            if(i ==0):
                header = row
                i = i+1
                continue
            temporary.append(row)
        csvfile.close()
    temporary.append(cas)
    with open('casi.csv','w', newline='') as csvfile:
        obj = csv.writer(csvfile)
        obj.writerow(header)
        obj.writerows(temporary)

def premor(odmor):
    odmor.append(datetime.now())
    zaccas = time.now()
    trenutno = 0
    while trenutno < 1800:
        trenutno = datetime.now()-zaccas
    return 0


print(datetime.now())
main()