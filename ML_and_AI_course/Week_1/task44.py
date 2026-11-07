a = [4, 9, 1, 7, 4]
def stats(nums):
    if not nums:
        return None
    s = ()
    minn = nums[0]
    maxx = nums[0]
    avg = 0

    for i in nums:
        if (i >= maxx):
            maxx = i
        if (i <= minn):
            minn = i
        avg += i
    s  += (minn,)
    s  += (maxx,)
    s  += (avg / len(nums),)
    return s
print(stats(a))