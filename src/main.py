stringEx = "ABCDCDC"
subStringEx = "CDC"
#print(len(subStringEx))
counter = 0

for i in range(0, len(stringEx) - (len(subStringEx) - 1)):
    #print(stringEx[i])
    stringTemp = ""
    for j in range(0, len(subStringEx)):
        stringTemp += stringEx[i+j]
    #print(stringTemp)  
    if stringTemp == subStringEx:
        counter += 1
print(counter)