# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True



def find_anagram(word, anagram):
    # [assignment] Add your code here
   
   if(len(word) == len(anagram)) and all(char in word for char in anagram):
       return True
   else:
      return False
  
        
print(find_anagram("boss", "bosu"))






