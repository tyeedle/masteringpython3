
import random
x = 10

print((lambda v : v * 2)(x))

names = ['John','David','James','Ethan']

d = {
    'Name1' : [],
    'Name2' : [],
    'Name3' : [],
    
}

d_Names = []
value = 0
for k,v in d.items():
    d[k].append(random.choice(names))
    
    d_Names.append(d[k])

print(d_Names[0])

