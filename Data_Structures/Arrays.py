'''Palindrome is a word that can be spelt the same way forward and backwards
Solving it  need:
Two pointers left and right which are going to move toward each other
left will start from index 0 and right will start from the last index.
if the pointers do not match output false otherwise True


'''
def check_palindrome(s):
    #change input to small letters
    s = s.lower()
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        left +=1
        right -=1

    return True
print(check_palindrome("Racecar"))
print(check_palindrome("Malayalam"))
print(check_palindrome("hello"))