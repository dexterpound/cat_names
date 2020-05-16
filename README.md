# cat_names
Python program that makes a list of cat names and then adds the index number to them.

```
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
    print(catNames[i])
    print(i)


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

```
Still needs to add index after the name and not on the next line.
