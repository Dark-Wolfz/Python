class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        arr = [[0]*n for k in range(m)]
        if obstacleGrid[0][0] == 0:
            arr[0][0]=1
        else:
            return 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    arr[i][j]=0
                else:
                    if i > 0:
                        arr[i][j] += arr[i-1][j]
                    if j > 0:
                        arr[i][j] += arr[i][j-1]
        return arr[m-1][n-1]
