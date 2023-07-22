class Solution:
    def mergeAlternately(self, word1, word2):
       k= len(word1)
       l= len(word2)
       i=j=0
       d=''
       while i<k or j<l:
         if i<k:
            d+=word1[i]
            i=i+1
         if j<l:
            d+=word2[j]
            j=j+1
       return d
