# function to check string is
# palindrome or not
def ispalindrome(str):
    # run loop from 0 to len/2
      for i in range (0,int(len(str)/2)):
       if str[i] !=str[len(str)-i-1]:
        return False
       return True
# main function
s = "malayalam"
ans =ispalindrome(s)

if (ans):
        print ("yes")
else:
        print("no")
