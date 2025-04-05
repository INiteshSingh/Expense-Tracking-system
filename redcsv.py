import csv
with open("C:\\Users\\nt984\\Desktop\\Strore Bill Data\\A2_ITEMS.csv", 'r', encoding='utf-8') as fp:
    csvdr=csv.DictReader(fp) # here csvdr is an object of <class 'csv.DictReader'>
    for dictrec in csvdr: # here dictrec is an object of <class, dict>
        for k,v in dictrec.items():
            print("\t{}-->{}".format(k,v))
        print()
        print("-"*50)