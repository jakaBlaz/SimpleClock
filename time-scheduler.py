from datetime import datetime as time
import csv

aktivnost = {
    "zaccas" : time.now(),
    "delo" : None,
    "csv" : [],
    "pavza-sum" : [0],
    "pavza-start" : [0],
    "pavza-stop" : [0],
    "konccas" : None,
}

def pavza():
    global aktivnost

    aktivnost["pavza-start"].append(time.now())

    while input("Ali je konec pavze?") == "Ne" or "ne":
        continue
    aktivnost["pavza-stop"].append(time.now())
    print(aktivnost["pavza-stop"][-1])
    summa = aktivnost["pavza-stop"][-1] - aktivnost["pavza-start"][-1]
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
    pavza()