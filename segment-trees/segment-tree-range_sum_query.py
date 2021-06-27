
    
# CodeForce problem
# https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/problem/A

# Leetcode : Range sum quey - mutable problem
# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3783/


####################
## Solution 1 : using Tree Structure
#####################

class Node :

    def __init__(self, val) :
        self.val= val
        self.left= None
        self.right= None
    
class NumArray:

    def __init__(self, nums) :
        self.length=0
        self.root= None

        if nums :
            self.length= len(nums)
            self.root= self._build_tree(nums, 0, self.length-1)

    # o(n) 
    def _build_tree(self, array, start, end) :
        if start > end :
            return None
        
        if start == end :
            return Node( array[start])
        
        mid= (start + end) // 2

        # Divide
        left= self._build_tree(array, start, mid)
        right= self._build_tree(array, mid+1, end)

        # Conquer
        node = Node(left.val + right.val)
        node.left= left
        node.right=right

        return node

    # O( lg n )
    def _update_node(self, idx, val, node, start, end):
        
        if (start > end ) :
            return
        
        if start == end  :
            node.val= val
            return
        
        mid= (start+end)//2

        if idx <= mid :
            self._update_node(idx, val, node.left, start, mid)
        else :
            self._update_node(idx, val, node.right,mid+1, end)

        node.val= node.left.val + node.right.val

        return
    
    # O(lg n)
    def _get_sum_range(self, node, i, j, s , e) :

        if s > e or i > j :
            return 0

        if s == i and e == j :
            return node.val if node else 0

        mid = (s+e) // 2

        if j<=mid :
            return self._get_sum_range(node.left, i,j,s,mid)
        if i> mid :
            return self._get_sum_range(node.right, i,j,mid+1, e)
        
        return self._get_sum_range(node.left, i,mid,s,mid) + self._get_sum_range(node.right, mid+1,j,mid+1,e) 
    
    def update(self, idx, val) :
        return self._update_node(idx, val, self.root, 0, self.length-1 )
    
    def sumRange(self, start, end) :
        return self._get_sum_range(self.root, start, end, 0, self.length-1)


#######################
# Solution 2 : Using Array Structure
#######################

class NumArray2 :

    def __init__(self, nums) :

        self.length=0
        self.data= None

        if nums :
            n= len(nums)
            sz= 1

            # To make the current array size to nearest power of 2
            while sz < n : sz *= 2

            self.length= sz
            self.data= [0] * 2 *self.length

            self._build_tree(nums,0, 0, sz-1)

    def _build_tree(self, array,pos, start, end) :

        # data = [0] * 2* len(array)
        
        if start == end :
            if start < len(array) :
                self.data[pos]= array[start]
            return
        
        mid= (start + end) // 2

        # Divide
        self._build_tree(array,2*pos+1, start, mid)
        self._build_tree(array,2*pos+2,  mid+1, end)

        # Conquer
        self.data[pos] = self.data[2*pos+1] + self.data[2*pos+2]
        # print(self.data)   

    def _update_node(self, idx, val, pos, start, end):
        
        if start > end :
            return
        
        if start == end  :
            self.data[pos]= val
            return
        
        mid= (start+end)//2

        if idx <= mid :
            self._update_node(idx, val, 2*pos+1, start, mid)
        else :
            self._update_node(idx, val, 2*pos+2,mid+1, end)

        self.data[pos] = self.data[2*pos+1] + self.data[2*pos+2]

        return
    
    def _get_sum_range(self, pos, i, j, s , e) :

        if s > e or i > j :
            return 0

        if s == i and e == j :
            return self.data[pos]

        mid = (s+e) // 2

        if j<=mid :
            return self._get_sum_range(2*pos+1, i,j,s,mid)
        if i> mid :
            return self._get_sum_range(2*pos+2, i,j,mid+1, e)
        
        return self._get_sum_range(2*pos+1, i,mid,s,mid) + self._get_sum_range(2*pos+2, mid+1,j,mid+1,e) 


    def update(self, idx, val) :
        return self._update_node(idx, val, 0 , 0, self.length-1 )
    
    def sumRange(self, start, end) :
        return self._get_sum_range(0, start, end, 0, self.length-1)

    

# Your NumArray object will be instantiated and called as such:
obj = NumArray2([3,1,2,5,6,4,3,2])
print(obj.update(5,8))
print(obj.sumRange(3,5))
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)