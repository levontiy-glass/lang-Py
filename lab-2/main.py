def add(nums, target):
    for i in range(len(nums)):
        temp = target - nums[i]
        for j in range(len(nums)):
            if j != i and temp == nums[j]:
                return([i, j])
                return