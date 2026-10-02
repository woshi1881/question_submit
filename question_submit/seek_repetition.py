import csv
with open ("./freelancer_2.csv","r",encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    id = []
    for row in reader:
        id.append(row["id"])
    for i in range(0,len(id)):
        for j in range(0,len(id[i])):
            if i != j:
                if id[i] == id[j]:
                    print("以下为重复")
                    print(id[i])
                    print(i)
                    print(id[j])
                    print(j)
                else:
                    continue
            else:
                continue



    