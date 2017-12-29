# find and replace
words = "It's thanksgiving day. It's my birthday,too!"
print words
words.find('day')
words.replace("day", "month", 1)

#min and max
x = [2,54,-2,7,12,98]
min(x)
max(x)

#first and last
x = ["hello",2,54,-2,7,12,98,"world"]
x[0]
x[len(x)-1]

#new list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
a = x[:len(x)/2]
b = x[len(x)/2:]
b.insert(0,a)
print b