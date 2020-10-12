import time
import csv

def premor():
    odmor[0] = time.strftime("%X")
    while 1:
        print("Želiš nadaljevati s projektom? Da/Ne")
        odg = input()
        if (odg.strip() == "Da") or (odg.strip() == "da"):
            odmor[1] = time.strftime("%X")
            return odmor
        else:
            time.sleep(1)

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

zacetni_cas = time.time()
dan = time.strftime("%d.%m.%Y, %A ,%X")
print("začel si ob: ", time.asctime(time.localtime()))
odmor = [0,0]
pavza = [0]
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
while True:
    print("si že končal?")
    try:
        konec = int(input("1 za ja ali 2 za premor: "))
        if konec == 1:
            #print("sem v if")
            break
        elif konec == 2:
            pavza.append(premor())
        else:
            konec = None
            time.sleep(1)
    except Exception as f:
        print(f) 
        konec = None
        time.sleep(1)

dan = dan + "," + time.strftime("%X")
dan = [dan,odmor[0],odmor[1]]
print("končal si ob: ", time.asctime(time.localtime()))
writeTimecsv(dan)

print(pavza)