while True:
    nums = sorted(list(map(int, input().split())))
    if nums[0] == nums[1] == nums[2] == 0:
        break
    if nums[0] + nums[1] <= nums[2]:
        print("Invalid")
    elif nums[0] == nums[1] == nums[2]:
        print("Equilateral")
    elif nums[0]==nums[1] or nums[1]==nums[2] or nums[2]==nums[0]:
        print("Isosceles")
    else:
        print("Scalene")
