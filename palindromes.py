def semordnilap(str1, str2):
    '''
    str1: a string, length > 1 and != str2
    str2: a string, length > 1 and != str1
    
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # Your code here
    if len(str1) != len(str2):
        return False
    elif str1 == "" and str2 == "": #base case
        return True
    else:            #recursive case 
        return str1[0] == str2[len(str2) - 1] and semordnilap(str1[1:],str2[:len(str2) - 1])
str1 = "palindromes"
str2 = "semordnilap"
print(semordnilap(str1,str2))