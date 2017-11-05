list_of_elements = [4, 2,4,4256,346,36,32623,6 235, 923, 52, 328]

x = int(input("Enter number to search: "))

found = F

for i in range(len(list_of_elements)):
    if (list_of_elements[i] == x):
        found = True
        print("%d spotted at %dth position" % (x, i))
        print("woooohooo")
        break

if (found == F):
    print("%d is not in list....maybe in another universe " % x)
