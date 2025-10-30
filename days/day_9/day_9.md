# Day #9 LeetCode problem

## Problem #9 Two Sum II - Input Array Is Sorted

Difficulty level: Medium  
[LeetCode link](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```
Example 2:
```
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
```
Example 3:
```
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 ```

Constraints:

2 <= `numbers.length` <= 3 * 10<sup>4</sup><br>
-1000 <= `numbers[i]` <= 1000 <br>
`numbers` is sorted in non-decreasing order. <br>
-1000 <= `target` <= 1000 <br>
The tests are generated such that there is exactly one solution.


### Companies asked this question in their job coding interview

| Time Period | Companies |
|--------------|------------|
| **0 – 3 months** | Microsoft (5), Google (3), Meta (2), Amazon (2) |
| **0 – 6 months** | Bloomberg (2) |
| **6 months ago** | Apple (10), Adobe (4), Yandex (4), Infosys (3), EPAM Systems (3), Oracle (2), TikTok (2), Zoho (2), Visa (2), Zomato (2) |