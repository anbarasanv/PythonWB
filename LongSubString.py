a = []
count=1
max_count =1
prev_char = None
b = input("Enter the string: ")
a=list(b.upper())
n=len(a)
result = {}
for i in range(0,n):
  curr_char = a[i]
  if(i>0):
    prev_char = a[i-1]
  if (curr_char == prev_char):
      count+=1
  else:
      count=1
  if (count > max_count):
      max_count = count
      result[curr_char]= max_count

print(result)
