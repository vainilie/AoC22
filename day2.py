my_file = open("input_day2.txt","r")
gaming = my_file.read()
gaming = gaming.split("\n")
puntaje = 0
# Rock 1pt A X
# Paper 2pt B Y 
# Scissors 3pt C Z
# 6 win 3 draw 0 lost
for game in gaming:
    gam = game.split(" ")
    if "X" in gam: #PERDER
        #puntaje += 1
        if "A" in gam:#ROCK1
            puntaje += 3
        elif "B" in gam:#PAPER2
            puntaje += 1
        elif "C" in gam:#TIJERA3
            puntaje += 2

    elif "Y" in gam: #DRAW
        puntaje += 3
        if "A" in gam:
            puntaje +=1
        elif "B" in gam:
            puntaje +=2
        elif "C" in gam:
            puntaje +=3
    elif "Z" in gam:
        puntaje += 6
        if "A" in gam:
            puntaje +=2
        if "B" in gam:
            puntaje +=3
        elif "C" in gam:
            puntaje +=1

        
print(puntaje)
