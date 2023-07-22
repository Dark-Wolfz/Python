class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
            largest = max(candies) #to find maximum value in the given list
            a = []
            i =0
            while i < len(candies):
               a.append(candies[i]+extraCandies) #to add element into list a
               i +=1
               result = []
            for candy in a:
               result.append(candy>=largest) #to produce boolean result list
            return result  
