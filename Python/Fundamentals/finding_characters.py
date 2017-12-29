# Finding characters assignment

# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list= []

# loop to find strings with "o" and append to new list
for i in range(0, len(word_list)):
    if word_list[i].find(char) != -1:
        new_list.append(word_list[i])

print new_list




