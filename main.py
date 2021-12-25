import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])


def return_a():
    for i,v in enumerate(a):
    
        dimensions = [f"{len(a)}x{len(a[i])}"]
    return [a,dimensions]


a_returned = return_a()[0]
a_returned_dimensions = return_a()[1]
print(a_returned)
print(a_returned_dimensions)

a2 = np.zeros(len(a))


b1 = np.array([1,2,3,4,5])
b2 = np.array([6,7,8,9,10])

b3 = np.concatenate((b1,b2))

def return_function(list_,excludeindex):
    s_ = sum(list_) - list_[excludeindex]
    return s_
    
returned_ = return_function(b3,1)



x = np.array([[5,6,7,8,9]])
y = np.array([[10,11,12,13,14]])



z = np.concatenate((x,y),axis=0)

for i in range(len(z)):
    dimensionsZ_ = [f'{len(z)}x{len(z[i])}']

