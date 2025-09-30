# 54. Spiral Matrix

**Difficulty:** Medium  
**Topics:** Array, Matrix, Simulation  
**Link:** [https://leetcode.com/problems/spiral-matrix/](https://leetcode.com/problems/spiral-matrix/)

---

## Problem Statement

Given an `m x n` matrix, return all elements of the matrix in spiral order.

**Example 1:**
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

**Example 2:**
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

**Constraints:**
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100

---

## Solution

**Intuition:**
Traverse the matrix in layers from outside to inside. For each layer, move right across top row, down right column, left across bottom row, and up left column. Track boundaries (top, bottom, left, right) and shrink them after completing each direction.

**Approach:**
- Initialize four boundaries: top, bottom, left, right
- While boundaries haven't crossed:
  - Traverse right: from left to right on top row, increment top
  - Traverse down: from top to bottom on right column, decrement right
  - Traverse left: from right to left on bottom row (if rows remain), decrement bottom
  - Traverse up: from bottom to top on left column (if columns remain), increment left
- Return result array

**Complexity:**
- **Time:** O(m × n) - visit every element exactly once
- **Space:** O(1) - excluding output array, only using boundary pointers

---

**Date:** Sept 30, 2025