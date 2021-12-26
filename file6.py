import numpy as np
import time
a = np.array([[1,2,3,4,5],[6,7,8,9,10]])

indexInLoop = 0
for i,v in enumerate(a):
    
    dimensions = f"{len(a)}x{len(v)}"


class linear_search_test:

    def __init__(self):
        print('Running')

    def linear_search(self,list,query):
        self.position = 0
        self.list = list
        self.query = query
        while self.position < len(self.list):
            print(self.list[self.position])
            if self.list[self.position] == self.query:
                print(f'found : query : {self.query} index : {self.list.index(self.position)}')
            self.position += 1
            time.sleep(0.1)
            

    def test(self,searchFor,listToSearch,**kwargs):
        self.searchFor = searchFor
        self.listToSearch = listToSearch    
        for k,v in kwargs.items():
            if k == "linear_search" and v == True:
                self.linear_search(self.listToSearch,self.searchFor)

            else:
                return

l = [1,2,3,5,6,5,7]

testing = linear_search_test()
testing.test(5,l,linear_search=True)

    