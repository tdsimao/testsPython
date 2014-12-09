

#a = [1, 11, 21, 1211, 111221, 
# look and say sequence
# font: http://en.wikipedia.org/wiki/Look-and-say_sequence

a = [1]

for i in range(30):
    x = a[-1]
    l = [int(n) for n in str(x)]
    j = 0
    l2 = []
    while j < len(l):
        count = 1
        value = l[j]
        j = j + 1
        while (j < len(l)) and (value == l[j]):
             count = count + 1
             j = j + 1
        l2.append(count)
        l2.append(value)     
    newNumber = int(''.join([str(n) for n in l2]))
    a.append(newNumber)
    print newNumber
print len(str(a[30]))
