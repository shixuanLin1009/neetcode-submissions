class Solution:
    def rob(self, nums: List[int]) -> int:
        
        mem_head={}
        mem_tail={}
        def f(i,num_list,mem):

            if i in mem :return mem[i]

            if i < 0:
                mem[i] = 0
                return mem[i]
            if i == 0:
                return num_list[i]
            if i == 1:
                return  max(num_list[0], num_list[1])
            
            
            mem[i] = max(num_list[i]+ f(i-2,num_list,mem),f (i-1,num_list,mem))
            return mem[i]
        
        if len(nums) == 1: return nums[0]

        # take head
        return max(f(len(nums[1:])-1, nums[1:], mem_head),f(len(nums[:-1])-1, nums[:-1], mem_tail))

# expected answer 3
# nums = [2, 3, 2],mem_head={},mem_tail={}
# max(f(len(nums[1:])-1, nums[1:], mem_head),f(len(nums[:-1])-1, num[:-1], mem_tail))
#   f(len(nums[1:])2-1, nums[1:][3,2], mem_head)->3
#       if i1 == 0 F
#       if i1 == 1 F
#       if i1 in mem F
#       mem[i] = max(num_list[i]1+ f(i-2-3,num_list,mem),f (i-1,num_list,mem))
#       f(-1)=0,f(0)=3
#   f(len(nums[:-1])-1, num[:-1], mem_tail)
#       if i1 == 0 F
#       if i1 == 1 F
#       if i1 in mem F
#       mem[i] = max(num_list[i]3+ f(i-2 -1,num_list,mem),f (i-10,num_list,mem))
#       f(-1)== f(0)=3