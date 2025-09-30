class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x, y = m - 1, n - 1
        
        for z in range(m + n - 1, -1, -1):
            if y < 0:
                break  # All elements from nums2 have been merged
            elif x < 0 or nums2[y] > nums1[x]:
                nums1[z] = nums2[y]
                y -= 1
            else:
                nums1[z] = nums1[x]
                x -= 1
        
      #  Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
       # Output: [1,2,2,3,5,6]
        
        
        
