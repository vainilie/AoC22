my_file = open("inputd4.txt","r")
data = my_file.read()
data = data.split("\n")
full = 0
partial = 0
for line in data:
    two = []
    if len(line) >0:
        rang = line.split(",")
        for ra in rang:
            limit = ra.split("-")
            ran = {*range(int(limit[0]) , int(limit[1]) + 1)}
            two.append(ran)
        if two[0].issubset(two[1]) or two[1].issubset(two[0]):
            full +=1
        if two[0].isdisjoint(two[1]) is False:
            partial +=1


  
# printing result
print(f"fully overlap: {full}")
print(f"overlap: {partial}")


