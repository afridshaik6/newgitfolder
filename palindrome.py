def is_palindrome(input_str):
    #calculate the str length
    str_length = len(input_str)
    for i in range(str_length//2):

        if not input_str[i]==input_str[str_length-1-i]:
            return False
    return True

print(is_palindrome('aaa'))
print(is_palindrome('aab'))