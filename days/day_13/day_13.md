# Day #13 LeetCode problem

## Problem #13 Number of Arithmetic Triplets

Difficulty level: Medium
[LeetCode link](https://leetcode.com/problems/number-of-arithmetic-triplets/description/)

You are given a 0-indexed, strictly increasing integer array `nums` and a positive integer `diff`. A triplet `(i, j, k)` is an arithmetic triplet if the following conditions are met:

`i < j < k`,<br>
`nums[j] - nums[i] == diff`, and<br>
`nums[k] - nums[j] == diff`.<br>
Return the number of unique arithmetic triplets.

 

Example 1:
```
Input: nums = [0,1,4,6,7,10], diff = 3
Output: 2
Explanation:
(1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
(2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 
```
Example 2:
```
Input: nums = [4,5,6,7,8,9], diff = 2
Output: 2
Explanation:
(0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
(1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.
``` 

Constraints:

3 <= `nums.length` <= 200 <br>
0 <= `nums[i]` <= 200<br>
1 <= `diff` <= 50<br>
`nums` is strictly increasing.

### Companies asked this question in their job coding interview

| Time Period | Companies |
|--------------|------------|
| **0 – 6 months** | Google (4), Meta (2) |