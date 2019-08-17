def count_sheeps(arrayOfSheeps):
    for i in range(len(arrayOfSheeps)):
        if arrayOfSheeps[i]==None:
            return "Undefined object found at "+str(i)+" position"
    return arrayOfSheeps.count(True)

