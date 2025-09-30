# 128. Longest Consecutive Sequence

**Difficulty:** Medium  
**Topics:** Array, Hash Table, Union Find  
**Link:** [https://leetcode.com/problems/longest-consecutive-sequence/](https://leetcode.com/problems/longest-consecutive-sequence/)

---

## Problem Statement

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

**Example 1:**
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4]. Therefore its length is 4.
**Example 2:**
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

**Constraints:**
- 0 <= nums.length <= 10⁵
- -10⁹ <= nums[i] <= 10⁹

---

## Solution

**Intuition:**
Convert array to a hash set for O(1) lookups. For each number, check if it's the start of a sequence (i.e., n-1 is not in the set). If it is, count how many consecutive numbers exist starting from that number. This ensures we only count each sequence once from its beginning.

**Approach:**
- Convert nums array to hash set
- For each number in the set:
  - Check if it's the start of a sequence (n-1 not in set)
  - If yes, count consecutive numbers (n, n+1, n+2, ...) while they exist in set
  - Track maximum length found
- Return longest sequence length

**Complexity:**
- **Time:** O(n) - each number visited at most twice (once to check start, once while counting)
- **Space:** O(n) - hash set stores all numbers

---

