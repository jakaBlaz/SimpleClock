from datetime import datetime as datum

import csv

aktivnost = {
    "zaccas" : datum.now(),
    "delo" : None,
    "csv" : [],
    "pavza-sum" : [0],
    "pavza-start" : [0],
    "pavza-stop" : [0],
    "konccas" : None,
}

def pavza():
    global aktivnost

    aktivnost["pavza-start"].append(datum.now())
    temp = True
    while temp:
        temp = int(input("Želiš nadaljevati s pavzo? 1 ali 0"))
    aktivnost["pavza-stop"].append(datum.now())
    summa = aktivnost["pavza-stop"][-1] - aktivnost["pavza-start"][-1]
    print(summa)
    aktivnost["pavza-sum"].append(summa)
    

aktivnost["delo"] = input("Kaj boš delal?")
print(f"Začel si ob {aktivnost['zaccas']} z : {aktivnost['delo']}")
with open('casi.csv','r', newline='') as csvfile:
        tempreader = csv.reader(csvfile,delimiter = ",",)
        i= 0
        for row in tempreader:
            if(i ==0):
                header = row
                i = i+1
                continue
            aktivnost["csv"].append(row)
        csvfile.close()

premor = True
while premor:
    premor = bool(int(input("ali še delaš? 1 za ja in 0 za ne")))
    if premor:
        brekfast = bool(int(input("Odmor? 1 za ja in 0 za ne")))
        if brekfast:
            pavza()

print("Die Ende")
print(aktivnost)