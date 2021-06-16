import os
import re
file_list = []
check = os.listdir('G:/flag/flag/')
ret = r'((flag|key|ctf){.*})'
for i in check:
    with open('G:/flag/flag/'+i,'r',encoding='utf-8') as f:
        a = f.read()
        res = re.findall(ret,a)
        if res:
            print('*'*66)
            print('[+]file_name: '+i)
            file_list.append('G:/flag/flag/'+i)
            
        else:
            continue
        
for y in file_list:
    with open(y,'r',encoding='utf-8') as file:
        files = file.read()
        print(re.findall(ret,files,re.IGNORECASE))