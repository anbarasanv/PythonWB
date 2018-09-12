#declare a list
li = [100,200,98,999,288]

#declaring the key function
def sumDigit(num):
  sum = 0
  while(num):
    sum += num%10
    num = int(num/10)
  return sum
#Printing the final filtered result
print("The higest sum:",max(li,key=sumDigit))
