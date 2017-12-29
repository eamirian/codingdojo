# Odd or Even
def odd_even(a, b):
    for i in range(a, b):
        if i % 2 == 0:
            print "Number is " + str(i) + ".  This is an even number."
        else:
            print "Number is " + str(i) + ".  This is an odd number."

#odd_even(1, 2000)

#Multiply
def multiply(list,num):
    for i in range(len(list)):
        list[i] *= num
    return list

a = [2,4,10,16]
b = multiply(a, 5)
#print b


#hacker challenge
def layered_multiples(arr):
    new_array = []
    for i in arr:
        temp = []
        for n in range(i):
            temp.append(1)
        new_array.append(temp)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x




