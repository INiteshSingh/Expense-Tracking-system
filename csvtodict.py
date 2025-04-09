import csv 
with open("C:\\Users\\nt984\\Desktop\\Strore Bill Data\\A2_ITEMS.csv","r") as fp:
    csvdr = csv.DictReader(fp)
    for dictrec in csvdr:
        for k,v in dictrec.items():
            print("\t{}--->{}".format(k,v))
        print()
        print("-"*50)

print(dictrec)