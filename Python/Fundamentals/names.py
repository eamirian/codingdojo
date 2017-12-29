#Part I
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names_output(students):
    for value in students:
        print value["first_name"], value["last_name"]

names_output(students)


#Part II
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def names_output2(users):
    for key, data in users.items():
        print key
        num = 1
        for value in data:
            name = "{} {}".format(value["first_name"].upper(),value["last_name"].upper())
            chars = len(name) - name.count(' ')
            print num,"-", name,"-",chars
            num += 1
            
names_output2(users)