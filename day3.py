import string
my_file = open("inputd3.txt","r")
gaming = my_file.read()
gaming = gaming.split("\n")
geton = []
suma = 0
eles = []
for ruck in gaming:
    if len(ruck) !=0:
        leng = int( (len(ruck)/2) )
        ruc1 = set(ruck[:leng])
        ruc2 = set(ruck[leng:])
        inter = ruc1.intersection(ruc2)
        intr = " ".join(inter)
        eles.append(intr)

#Part 2
chunks = [gaming[x:x+3] for x in range(0,len(gaming), 3)]
teams=[]
for chunk in chunks:
    if len(chunk) == 3:   
        s1=set(chunk[0])    
        s2=set(chunk[1])
        s3=set(chunk[2])
        inters = (s1&s2&s3)
        inte = "".join(inters)
        teams.append(str(inte))
print(teams)
alpha = dict(enumerate(string.ascii_letters, 1))
for tea in teams:
    valu = [k for k, v in alpha.items() if v == tea]
    suma += int(valu[0])
print(suma)

