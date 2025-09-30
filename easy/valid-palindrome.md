# 125. Valid Palindrome

**Difficulty:** Easy  
**Topics:** Two Pointers, String  
**Link:** [https://leetcode.com/problems/valid-palindrome/](https://leetcode.com/problems/valid-palindrome/)

---

## Problem Statement

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

**Example 1:**
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
**Example 2:**
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

**Constraints:**
- 1 <= s.length <= 2 × 10⁵
- s consists only of printable ASCII characters

---

## Solution

**Intuition:**
Use two pointers starting from both ends of the string. Skip non-alphanumeric characters and compare characters (case-insensitive). If any pair doesn't match, it's not a palindrome. If pointers meet without mismatch, it's valid.

**Approach:**
- Initialize left pointer at start, right pointer at end
- While left < right:
  - Skip non-alphanumeric characters from left
  - Skip non-alphanumeric characters from right
  - Compare characters (convert to lowercase)
  - If they don't match, return False
  - Move both pointers inward
- Return True if loop completes

**Complexity:**
- **Time:** O(n) - single pass with two pointers
- **Space:** O(1) - only using two pointer variables

---

**Date:** Sept 30, 2025