
nums = list(map(int, input().split()))

while nums != sorted(nums):
    i = 0
    while i < 4:
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            print(*nums)
        i += 1
