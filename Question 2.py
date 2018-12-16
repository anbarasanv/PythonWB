groups = []
same_id = []
queries = []
t = 0
test = int(input())
line2 = input()
line3 = input()
line2 = line2.split(" ")
line2 = [int(i) for i in line2]
line3 = line3.split(" ")
Arr = [int(i) for i in line3]


for i in range(line2[1]):
    inp = input()
    inp = inp.split(" ")
    inp = [int(j) for j in inp]
    queries.append(inp)

def checkgroup(students):
    ind = []
    for i in range(len(groups)):
        for j in range(2):
            if(students[j] in groups[i]):
                ind.append(i)
    return ind


def combinegroup(same_id, groups):
    tmp = []
    dgroup = []
    
    for i in same_id:
        tmp += groups[i]
    tmp = list(tmp)
    
    for j in range(len(groups)):
        if j not in same_id:
            dgroup.append(groups[j])
    
    dgroup.append(tmp)
    
    return dgroup

def maxvalueCheck(gr):
    maxval = 0
    for i in range(len(gr)):
        for k in gr[i]:
            if(Arr[k-1] > maxval):
                maxval = Arr[k-1]
    return maxval

def primeFinder(gr):
    count = 0
    lengths = []
    flag = True
    for i in gr:
        lengths.append(len(i))
    for j in lengths:
        if(j == 2 or j==3):
            count +=1
        else:
            end = int(j ** 0.5)
            for i in range(2,end+1):
                if(j%i == 0):
                    flag = False
            if(flag):
                count +=1
    return count

def productFinder(gr):
    lengths = []
    product = 1
    
    for i in gr:
        lengths.append(len(i))
    for j in lengths:
        product *= j
    
    return product
while(t < test):      
    for i in range(len(queries)):
        if(i==0):
            groups.append(queries[i])
            H = maxvalueCheck(groups)
            C = primeFinder(groups)
            P = productFinder(groups)
            print(H,C,P)
        else:
            same_id = checkgroup(queries[i])
            if(len(same_id) == 2):
                groups = combinegroup(same_id, groups)
                H = maxvalueCheck(groups)
                C = primeFinder(groups)
                P = productFinder(groups)
                print(H,C,P)
            else:
                groups.append(queries[i])
                H = maxvalueCheck(groups)
                C = primeFinder(groups)
                P = productFinder(groups)
                print(H,C,P)
    t +=1
        
    

   
