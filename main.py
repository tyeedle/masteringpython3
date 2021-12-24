import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])


for i in range(len(a)):
    print(a[i])
    

    dimensions = [f"{len(a)}x{len(a[i])}"]

a2 = np.zeros(len(a))
print(a2)

b1 = np.array([1,2,3,4,5])
b2 = np.array([6,7,8,9,10])

b3 = np.concatenate((b1,b2))

def return_function(list_,excludeindex):
    s_ = sum(list_) - list_[excludeindex]
    return s_
    
returned_ = return_function(b3,1)
print(b3[1] + returned_)
