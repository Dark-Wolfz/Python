class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        ch = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                # Check if the current position is at the edges or the next position is 0 (valid position to plant flower)
                if i == 0 or flowerbed[i - 1] == 0:
                    if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                        ch += 1
                        flowerbed[i] = 1  # Place a flower at the current position
                        if ch == n:
                            return True
            i += 1

        return ch >= n
