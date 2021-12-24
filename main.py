import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
position = 0

for i in range(len(a)):
    print(a[i])
    

    dimensions = [f"{len(a)}x{len(a[i])}"]

print(dimensions)