# Advanced-Python-Programming
Advanced Python Programming course repository with Python concepts, loops, patterns, functions, data structures, file handling, exception handling, OOP, modules, assignments, practice programs, and practical implementations.


              class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_depth = 0
        current_depth = 0
        
        for char in s:
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1
                
        return max_depth
  
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_depth = 0
        current_depth = 0
        
        for char in s:
            if char == '(':
                current_depth += 1class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_depth = 0
        current_depth = 0
        
        for char in s:
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1
                
        return max_depth
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1
                
        return max_depth
