with open("input.txt", "r+") as file1:
    # Reading form a file
    data = file1.read()
    elfs =[]
    datas = data.split("\n\n")
    for ele in datas:
        el = ele.split("\n")
        count = 0
        for esy in el:
            if len(esy) >0:
                count += int(esy)
        elfs.append(count)
    elfs.sort(reverse = True)
    print(elfs)
    print(elfs[0] + elfs[1] +elfs[2])
