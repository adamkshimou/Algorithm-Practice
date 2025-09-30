# 238. Product of Array Except Self

**Difficulty:** Medium  
**Topics:** Array, Prefix Sum  
**Link:** [https://leetcode.com/problems/product-of-array-except-self/](https://leetcode.com/problems/product-of-array-except-self/)

---

## Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

**Example 1:**
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

**Example 2:**
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

**Constraints:**
- 2 <= nums.length <= 10⁵
- -30 <= nums[i] <= 30
- The product of any prefix or suffix is guaranteed to fit in a 32-bit integer

**Follow up:** Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space)

---

## Solution

**Intuition:**
For each position, the answer is the product of all elements to its left multiplied by the product of all elements to its right. Use two passes: first calculate prefix products (left to right), then multiply by postfix products (right to left) in the same result array.

**Approach:**
- Initialize result array with all 1s
- First pass (prefix): traverse left to right
  - Store prefix product at each position
  - Update prefix by multiplying with current element
- Second pass (postfix): traverse right to left
  - Multiply each position by postfix product
  - Update postfix by multiplying with current element
- Result array now contains products except self

**Complexity:**
- **Time:** O(n) - two passes through array
- **Space:** O(1) - excluding output array, only using two variables (prefix, postfix)

---

**Date:** Sept 30, 2025