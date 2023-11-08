def twoSum(self, nums, target):
    map = {}
    for k, v in enumerate(nums):
        if not map.get(v):
            map[v] = k
        else:
            map[str(v)] = k

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in map.keys() and diff != nums[i] or str(diff) in map:
            return [i, map[diff]]