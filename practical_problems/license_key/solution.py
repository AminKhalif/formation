
# Solution is wrong , review the problem
# https://leetcode.com/problems/license-key-formatting/solutions/


def licenseKeyFormatting(license: str, k:int) ->str:
    split_index = license.find('-')
    count = 0
    
    initial_string = (license[0: split_index]).upper()
    remainder_string = license[split_index+1:].upper().replace("-", "")
    final_string = ''
    full_cleaned_string = initial_string + remainder_string
    
    
    if len(full_cleaned_string) %k == 0:
        
        for char in full_cleaned_string:
            if count == k:
                final_string += '-' + char
                count = 0
            else:      
                final_string += char
                count+=1        
    
        return final_string  
    
    else:
        
        for char in remainder_string:  
            if count == k:
                final_string += '-' + char
                count = 0
            else:      
                final_string += char
                count+=1
    
    final_string = initial_string + "-" + final_string
    return final_string    

s ="2-5g-3-J"


k = 2

print(licenseKeyFormatting(s, k))  # Expected : "24A0-R74K" My output : "2-4A0R-74K"




'''

Run through of code

remainder_string = 5G3J

Loop1 
count = 0
str = 5


Loop2
count =1
str 5G

Loop 3 
count = 2
str = 5G-

Loop 4 
count = 0


'''