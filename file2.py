import time
import random
array_ = ['log1','log2','error1']
txt_ = 'txtFiles/newfile.txt'

def writeToTxtFile(txt_file,text):
    with open(txt_file,'w') as f:
        f.write(f'{text}\n')

while True:
    writeToTxtFile(txt_,random.choice(array_))
    time.sleep(0.1)

