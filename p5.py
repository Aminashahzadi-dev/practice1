def stats(nums):
    return min(nums), max(nums), sum(nums) / len(nums)


lo, hi, avg = stats([4, 8, 15, 16, 23, 42])
print(lo, hi, avg)


def grade(marks, passing=50):
    return "Pass" if marks >= passing else "Fail"


print(grade(55))
print(grade(55, passing=60))
