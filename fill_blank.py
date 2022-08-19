def fill_blanks(nums):
    nums_without_blank= []
    for i in nums:
        if i is None:
            nums_without_blank.append(0)
        else:
            nums_without_blank.append(i)
    return nums_without_blank
