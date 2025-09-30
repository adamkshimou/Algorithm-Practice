# 217. Contains Duplicate

**Difficulty:** Easy  
**Topics:** Array, Hash Table, Sorting  
**Link:** [https://leetcode.com/problems/contains-duplicate/](https://leetcode.com/problems/contains-duplicate/)

---

## Problem Statement

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

**Example 1:**
Input: nums = [1,2,3,1]
Output: true

**Example 2:**
Input: nums = [1,2,3,4]
Output: false

**Constraints:**
- 1 <= nums.length <= 10⁵
- -10⁹ <= nums[i] <= 10⁹

---

## Solution

**Intuition:**
Use a hash set to track numbers we've seen. As we iterate through the array, check if the current number already exists in the set. If yes, we found a duplicate. If we finish the loop without finding duplicates, all elements are unique.

**Approach:**
- Create empty hash set
- For each number in array:
  - If number exists in hash set, return True (found duplicate)
  - Otherwise, add number to hash set
- If loop completes, return False (no duplicates found)

**Complexity:**
- **Time:** O(n) - single pass through array with O(1) hash set operations
- **Space:** O(n) - hash set stores up to n unique elements

---
