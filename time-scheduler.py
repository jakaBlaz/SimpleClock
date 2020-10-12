from datetime import datetime as time
import csv

aktivnost = {
    "zaccas" : time.now(),
    "delo" : None,
    "pavza" : [],
    "konccas" : None,
}

aktivnost["delo"] = input("Kaj boš delal?")
print(f"Začel si ob {aktivnost['zaccas']} z : {aktivnost['delo']}")

