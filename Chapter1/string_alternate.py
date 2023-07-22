class Solution:
    def mergeAlternately(self, word1, word2):
       i=j=0
       d=''
       while i<len(word1) or j<len(word2):
         if i<len(word1):
            d+=word1[i]
            i=i+1
         if j<len(word2):
            d+=word2[j]
            j=j+1
       return d
