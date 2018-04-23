
# coding: utf-8

# In[ ]:


def len_members(list_members):
    len_list = []
    for mem in list_members:
        len_list.append(len(mem))
    return len_list

user_input = input("Please enter the list of members separated by space: ")
print("The length of the members in the input list is: ", len_members(user_input.split()))

def check_vowel(input_char):
    if(input_char in "aeiou"):
        return True
    else:
        return False
input_c = input("Please enter a single character for vowel checking: ")    
print(input_c, " is a vowel: ", check_vowel(input_c))
        
        

