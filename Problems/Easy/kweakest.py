class Solution(object):
    def kWeakestRows(self, mat, k):
        m, n = len(mat), len(mat[0])
        a = []
        for i in range(m):
            count = 0
            for j in range(n):
                if mat[i][j] == 1:
                    count += 1
            a.append((i, count))
        for i in range(len(a)):
            for j in range(0, len(a) - i - 1):
                if a[j][1] > a[j + 1][1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        weakest_rows_indices = [x[0] for x in a[:k]]

        return weakest_rows_indices

        
