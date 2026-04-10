class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binarySearch(st: int, t: int) -> int:
            s,e = st,len(numbers) - 1
            
            while s <= e:
                mid = int((s + e) / 2)
                if numbers[mid] < t:
                    s = mid + 1
                elif numbers[mid] > t:
                    e = mid - 1
                else:
                    return mid
            return -1

        for i, e in enumerate(numbers):
            temp = binarySearch(i + 1, target - e)
            if temp != -1:
                return [i+1,int(temp)+1]
        return -1
        