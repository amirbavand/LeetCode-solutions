class Solution:
    def trimMean(self, arr):
        arr.sort()
        lenght = len(arr)
        print(len(arr))
        lenght5Percent = int(len(arr)/20)
        arr_sum = sum(arr[lenght5Percent:lenght-lenght5Percent])
        print(arr_sum/(lenght-(2*lenght5Percent)))
        print(arr)
        return(arr)


arr = [6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4,
       8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10, 8, 2, 3, 4]
a = Solution()
a.trimMean(arr)
