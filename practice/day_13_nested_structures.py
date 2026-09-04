print('='*40)
print('LIST OF DICTIONARIES')
print('='*40)

subject = [{'name':'Athul','mark':85,'subject':'AI'},
            {'name':'Swetha','mark':81,'subject':'AGRI'},
             {'name':'milan','mark':71,'subject':'CSE'}
             
            ]

print('Student Database')
for i in subject:
    print(f"-{i['name']} Scored {i['mark']} in {i['subject']}")

print('='*40)
print('DICTIONARY WITH LIST')
print('='*40)

course = {'AI':['python','ML','DL'],'WEB': ['HTML','CSS','JS']}
print(course)
print(f"AI subject: {course['AI']}")
print(f"First AI subject: {course['AI'][0]}")

print('='*40)
print('ADD A NEW STUDENT')
print('='*40)

new = input('Enter student name:')
new1 = int(input('Enter Mark:'))
new2 = input('Enter Subject')

subject.append({'name':new,'mark':new1,'subject':new2})
for i in subject:
    print(f"{i['name']} scored {i['mark']} in {i['subject']}")