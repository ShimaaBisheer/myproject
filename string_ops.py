def find_nth_occurrence (string, substring, occurrence=1):
    ix = -1
    for _ in range(occurrence):
        ix = string.find(substring, ix+1)
        if ix == -1:
            return -1
    return print(ix)





import re
def solve(a,b):
    return bool(re.fullmatch(a.replace('', '.'), b))
print(solve("code*warrior","codewars"))




def is_palindrome(text):
    text = text.replace(' ', '') 
    text = text.upper() 
    
    if len(text) >0:
        if text == text[::-1]:
            return True
        else:
            return False
    else:
        print('empty string')
print(is_palindrome("kakak"))



'''
def ret_repeated(string_check):
    sub_string_count=[]
    for i in range (len(string_check)):
        sub_string_count.append(string_check.count(string_check[:i+1], 0, len(string_check)))
    return max(sub_string_count), string_check[0:get_last_max_index(sub_string_count)+1]

def get_last_max_index(list_):    
    for i in range (len(list_)-1):
        if (list_[i+1] < list_[i] ):
            return i
        
    return len(list_)
ret_count, ret_str = ret_repeated("abcde")
var = (ret_str, ret_count)
'''






