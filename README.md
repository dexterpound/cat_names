
````
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are:')
#for name in range(len(catNames)):
    #print(name)

for i in range(len(catNames)):
    
    
    print(catNames[i], " : ", str(i))
    #print(catNames[i] + " " + str(i))
    #print(str(i),":",catNames[i])
    #print(catNames[i], " : ", str(i))
    #print(catNames[i], i, end=' ')
    #print(catNames[i],end=' ' + str(i))
    #print(catNames[i], i)
    #print(f"{catNames[i]} {str(i)}")
````
