# 88. Merge Sorted Array

**Difficulty:** Easy  
**Topics:** Array, Two Pointers, Sorting  
**Link:** [https://leetcode.com/problems/merge-sorted-array/](https://leetcode.com/problems/merge-sorted-array/)

---

## Problem Statement

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to 0 and should be ignored. `nums2` has a length of `n`.

**Example 1:**

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6].

**Example 2:**
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]

**Constraints:**
- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -10⁹ <= nums1[i], nums2[j] <= 10⁹

---

## Solution

**Intuition:**
Fill nums1 from the end backwards using three pointers. Since both arrays are sorted, compare elements from the end of each array and place the larger one at the end of nums1. This avoids overwriting elements in nums1 that haven't been processed yet.

**Approach:**
- Start with three pointers: x (end of nums1 elements), y (end of nums2), z (end of merged array)
- Iterate backwards from position m+n-1 to 0
- Compare nums1[x] and nums2[y], place the larger element at nums1[z]
- Move the corresponding pointer backward
- Continue until all nums2 elements are merged (nums1 elements already in correct position)

**Complexity:**
- **Time:** O(m + n) - single pass through both arrays
- **Space:** O(1) - merging in-place, no extra space

---