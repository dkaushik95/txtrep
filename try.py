import csv
final = {}
ofile = open('ttest.csv', "wb")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
with open("try.csv", "rb") as f:
    reader = csv.reader(f)
    roww = []
    for row in reader:
        if row[0] == "name":
            continue
        else:
            roww.append(row[0])
            for x in xrange(1, 5):
                one = row[x].split("-")
                roww.append(one[0])
                try:
                    roww.append(one[1])
                except:
                    print("error")
            print roww
            final[row[0]] = roww
            writer.writerow(roww)
            roww = []
ofile.close()
