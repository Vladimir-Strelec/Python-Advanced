def palindrome(text, num=0, left_indx=-1):
    if len(text) // 2 == num:
        return f"{text} is a palindrome"

    if text[num] == text[left_indx]:
        return palindrome(text, num+1, left_indx - 1)
    else:
        return f"{text} is not a palindrome"


print(palindrome('abcba', 0))
#print(palindrome('peter', 0))