# Solution for problem #1 
## Question
![LeetCode Problem 1 screenshot](res/LeetCode%20problem_1.png)
---
**Question:** To find two numbers in an array whose sum is equal to the target value. We asked to return the postion/indices of the two numbers.
### Two approaches
#### 1. Brute force method.  

We take each pair of elements in the array and check if their sum is equal to the target value. 
We implement using a nested loop ( a loop inside a loop)
The outer loop iterates from the first element to the last element, and the second loop from the next element to the last element <br>
##### Visually 
![Visual demonstration of brute force approach](res/brute%20force.gif)

#### Implementation in Python
```
class Solution:
    def twoSum(self, nums: List[int], target: int) ->   List[int]:
	    n=len(nums)
	    for i in range(n): #Loop through each number 
		    for j in range(i+1, n): # Check all number after i
			    if nums[i] + nums[j] == target: # dot they add to the target
				return[i,j] # yes return their indices
	    return [] # if no solution found, return empty array
```
**Time complexity:** the outer loop runs n times and the inner loops run up to n-1 times <br>
- Total = n * n = O(n<sup>2</sup>) <br>

**Space complexity:** no extra data structure used so O(1)

#### 2. HashMap approach: efficient

We iterate the array only once. For each element, we check if the target minus the current element exists in the hash table. 
Steps
1. Create an empty hash map/ dictionary in Python to store elements and their indices.
2. iterate through array/list left to right starting from index 0
3. For each element nums[i] calculate the complement by subtracting from the target. complement = target - nums[i]
4. Check if the complement exists in the hash table. if yes, we found the solution, return the current element index and the index from the hash map 
5. If the complement does not exist in the hash table, add the current element nums[i] and its index into the hash table
6. Repeat steps 3-5 until we find a solution or reach the end of the array
7. If no solution found, return an empty array 

#### Implementation in python
```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        # Return an empty list if no solution is found
        return []
```
**With detailed comment** 

```
class Solution:
    
    # Define the twoSum function that takes:
    # - nums: a list of integers
    # - target: the target integer we want to find the sum for
    # It returns a list of two indices from nums whose values add up to target.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Create an empty dictionary (hash map) to store numbers we've seen so far
        # Key   → the number itself (nums[i])
        # Value → the index of that number (i)
        hashmap = {}
        
        # Loop through each index 'i' in the nums list
        for i in range(len(nums)):
            
            # Calculate the number needed to reach the target
            # For example, if target = 9 and nums[i] = 2 → complement = 7
            complement = target - nums[i]
            
            # Check if this complement number has already been seen
            # (i.e., if it's stored in our hash map)
            if complement in hashmap:
                # If found, that means:
                # nums[i] + nums[hashmap[complement]] = target
                # Return their indices as a list
                return [i, hashmap[complement]]
            
            # Otherwise, store the current number and its index in the hash map
            # This helps us check future numbers against it
            hashmap[nums[i]] = i
        
        # If we finish looping and no pair adds up to the target,
        # return an empty list (this line is rarely reached 
        # because the problem guarantees one solution)
        return []
```

**Time complexity** = O(n) iterate throught array once <br>
**Space complexity** = O(n) extrash hash table required to store complements

