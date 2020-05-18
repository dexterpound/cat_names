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

    #print(f"{catNames[i]} {str(i)}")
    print(catNames[i], " : ", str(i))
    #print(catNames[i] + " " + str(i))
    #print(str(i),":",catNames[i])
    #print(catNames[i], " : ", str(i))
    #print(catNames[i], i, end=' ')
    #print(catNames[i],end=' ' + str(i))
    #print(catNames[i], i)


#catNames = ['a', 'b', 'c', 'd']
#             0    1    2    3
#for i in range(len(catNames)):  i will go from 0, 1, 2, 3
    #print(i) i is the index
    #print(catNames[i]) catNames[i] is the element at index i

# the output will be:
#0
#'a'
#1
#'b'
#2
#'c'
#3
#'d'