# 20. Valid Parentheses

**Difficulty:** Easy  
**Topics:** String, Stack  
**Link:** [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/)

---

## Problem Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**
Input: s = "()"
Output: true

**Example 2:**
Input: s = "(]"
Output: false

**Constraints:**
- 1 <= s.length <= 10⁴
- s consists of parentheses only '()[]{}'

---

## Solution

**Intuition:**
Use a stack to track opening brackets. Every time we see a closing bracket, it must match the most recent opening bracket (top of stack). If they match, pop the stack. If the string is valid, the stack should be empty at the end.

**Approach:**
- Create empty stack and mapping of closing → opening brackets
- For each character:
  - If it's a closing bracket: check if stack top matches, if not return False
  - If it's an opening bracket: push to stack
- After loop, stack should be empty (all brackets matched)


Complexity:

Time: O(n) - single pass through string
Space: O(n) - stack stores up to n/2 opening brackets in worst case