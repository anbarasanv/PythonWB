class StringConverter:
    ''' This the String case converter class'''
    #The below is called mask which will used with operation of conversion
    mask = ord(' ')
    
    #The below function get the lowercase as input and returns uppercase as output
    def lowertoUpper(self,instr):
        '''This function takes lower case string and retuns upper case string'''
        result = [] #The Result will be stored in this list
        templist = [ord(x) for x in instr] # converting all the strings to decimal
        for i in templist:
            temp = i & ~self.mask #The logic behind the conversion
            result.append(chr(temp)) #Appending each coverted character to the result list
        return ''.join(result) #Returning the result list as a string
        
    #The below function get the uppercase as input and returns lowercase  as output    
    def uppertoLower(self,instr):
        '''This function takes upper case string and retuns lower case string'''
        result = [] #The Result will be stored in this list
        templist = [ord(x) for x in instr] # converting all the strings to decimal
        for i in templist:
            temp = i | self.mask #The logic behind the conversion
            result.append(chr(temp)) #Appending each coverted character to the result list
        return ''.join(result) #Returning the result list as a string

obj = StringConverter()
value = obj.lowertoUpper("ANBA")
value1 = obj.uppertoLower("anba")
print(value, value1)
