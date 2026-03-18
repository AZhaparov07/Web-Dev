def centered_average(nums):
    nums_sorted = sorted(nums)
    nums_centered = nums_sorted[1:-1]
    return sum(nums_centered) // len(nums_centered)