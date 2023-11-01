student={1:{'name':'sneara','age':23,'sex':'female'},
         2:{'name':'mehrima','age':2,'sex':'female'},
         4:{'name':'jimi','age':3,'sex':'female'}


       }

print(student[1]['sex'])
print(student[2]['name'])
print(student[4]['age'])

student[3]={}
student[3]['name']={'jannat'}
student[3]['age']={'5'}
student[3]['sex']={'female'}
print(student[3])
del student[3]['sex']
print(student[3])
