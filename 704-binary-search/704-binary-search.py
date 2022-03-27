class Solution:
    def search(self, nums: List[int], target: int) -> int:
        flag  = False
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high) //2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums [mid]:
                high = mid - 1
            elif target == nums[mid]:
                return mid
        if flag == False:
            return -1