nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
while True:
    try:
        target = int(input('Введите число :'))
    except:
        print("Только числа!")
    c = 0
    for i in nums:
        if i == target:
            c = 1
            break
    if c == 0:
        print(-1)
    if c == 1:
        print(nums.index(target))