import re 
import sys

def timeConversion(s):
  r = re.sub(r'([0-9])(:)','',s)
  sp=re.sub(r'[A-Za-z]+','',s)
  ap=re.sub(r'[0-9]','',r)
  if ap == 'AM':
    return sp
  elif ap == 'PM':
    cal = list(map(int,sp.split(":")))
    cal[0] = cal[0]+12
    cal1 = sp.split(':')
    cal1[0]=str(cal[0])
    so=cal1[0]+":"+cal1[1]+":"+cal1[2]
    return so
    # Complete this function

s =input().strip()
result = timeConversion(s)
print(result)
