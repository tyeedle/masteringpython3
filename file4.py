l = [1,2,3,4,5,6,1,2]

def replace_item_in_list(list,query,replacingValue,**printout):
    for i,v in enumerate(list):
        if v == query:
            list[i] = replacingValue
            
    for k,v in printout.items():
        if k == 'printout' and v == True:
            print(f'out : {list}')
        else:
            return
    return list
         
    

new_list = replace_item_in_list(list=l,query=1,replacingValue=100,printout=True)