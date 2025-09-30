# 242. Valid Anagram

**Difficulty:** Easy  
**Topics:** Hash Table, String, Sorting  
**Link:** [https://leetcode.com/problems/valid-anagram/](https://leetcode.com/problems/valid-anagram/)

---

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**
Input: s = "anagram", t = "nagaram"
Output: true
**Example 2:**
Input: s = "rat", t = "car"
Output: false

**Constraints:**
- 1 <= s.length, t.length <= 5 × 10⁴
- s and t consist of lowercase English letters

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution?

---

## Solution

**Intuition:**
Two strings are anagrams if they contain the same characters with the same frequencies. Use two hash maps to count character frequencies in both strings, then compare the maps. If lengths differ, they can't be anagrams.

**Approach:**
- Check if lengths are equal, return False if not
- Create two hash maps (countS, countT)
- Iterate through both strings simultaneously:
  - Count frequency of each character in s
  - Count frequency of each character in t
- Compare the two hash maps for equality

**Complexity:**
- **Time:** O(n) - single pass through both strings where n is length
- **Space:** O(1) - hash maps store at most 26 characters (lowercase English letters)

---

