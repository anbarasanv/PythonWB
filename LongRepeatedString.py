#!/usr/bin/python
import re
ch ="aaadd"
result = {}
finder = re.findall(r'(\w)\1{1,}',ch)
for i in finder:
    key =i
    regv=i+"+"
    res = re.search(regv,ch)
    value= len(res.group())
    result[key] = value
print(result)
if (len(result) >=2):
    print("There are multiple chars repeated max at same times!!!")
    for x in result:
        print("The repeated string:",x,":",result[x])

else:
    maximum = max(result,key=result.get)    
    print("The most repeated value is:",maximum,":",result[maximum])
    
