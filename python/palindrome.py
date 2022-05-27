import re 
def palindrome(word):
    word = str(word).lower()
    word_list=[]
    
    for letter in word:
        if re.search("[a-z0-9]",letter) != None :
            word_list.append(letter)
   
    rev_list= word_list.copy()
    rev_list.reverse()
    
    if "".join(word_list) == "".join(rev_list):
        return True
    else:
        return False    
    
