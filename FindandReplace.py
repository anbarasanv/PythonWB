def FindandReplace(instr):
    """
    This function only Find and replaces the strings of same length
    Which means Find string length and replacement string must be same
    """
    #Getting user Input Search string and replacement string
    s1 = input("Enter the string Need to be replaced: ")
    s2 = input("Enter the string Need to be replaced with: ")
    #using the string maketranslate for replacement object
    t = str.maketrans(s1,s2)
    #sending input as argument
    out = instr.translate(t)
    #Returning the results
    return out
def main():
    instr = input("Enter the Paragraph for Testing ")
    result = FindandReplace(instr)
    print(result)
if __name__  == '__main__':
    main()
