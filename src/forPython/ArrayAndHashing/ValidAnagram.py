'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false

Hint: Anagram example: abcc & cbca
'''

'''
Thoughts:
For this question, once we unerstand what is anagram, it's basically asking us to count how many of each characters in s and t.
So we can use a HashMap here:
s:          t:
a  3         a  3
n  1         n  1
g  1         g  1
r  1         r  1
m  1         m  1

Time Complexity = O(n)/ O(s+t)
Memory Comlexity = O(n)/ O(s+t)

When it comes to compare two strings, sorting might create a way to the result:
so we just sort the two strings, and comapre them to see if they are eqaul.
**Try to write a sort function yourself in case of interview requirement

Other than that, there is another way in python can do it:
return Counter(s) == Counter(t),
this can automatically count and compare, but not a good way for interview though
'''

class ValidAnagram():
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True
    
va = ValidAnagram()
print(va.isAnagram(s= "anagram", t= "nagaram"))

# Well Explained Version
class ValidAnagram():
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagram: same length
        if len(s) != len(t):
            return False
        
        # Create HashMap
        countS, countT = {}, {}

        # Iterate two strings and count
        # Same length, choose whichever
        for i in range(len(s)):
            # You cannot just write countS[s[i]] = 1 + countS[s[i]] here because when 
            #   the character does not in the HashMap yet, it will through a key error
            #   with this function: countS.get(s[i], 0), if the key doesnt in the HashMap,
            #   the defaul value this function gonna return is 0
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # Iterate the HashMap
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True
    
va = ValidAnagram()
print(va.isAnagram(s= "anagram", t= "nagaram"))