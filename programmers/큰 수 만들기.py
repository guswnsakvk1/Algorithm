def solution(number, k):
    nums = []
    
    for i in number:
        while k > 0 and nums and nums[-1] < i:
            nums.pop()
            k -= 1
        nums.append(i)
        
    if(k>0):
        nums = nums[:-k]

    return ''.join(nums)