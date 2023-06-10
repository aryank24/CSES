n = int(input())
c = 0
nums = list(map(int, input().split()))
for i in range(len(nums)-1):
    if nums[i] > nums[i+1]:
        c += nums[i] - nums[i+1]
        nums[i+1] = nums[i]
print(c)