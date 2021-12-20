import sys


if __name__ == '__main__':
    nums = [int(i) for i in sys.argv[1:]]
    number = int(sum(nums) / len(nums))
    count = 0
    for i in range(len(nums)):
        if nums[i] > number:
            while nums[i] != number:
                nums[i] -= 1
                count += 1
        elif nums[i] < number:
            while nums[i] != number:
                nums[i] += 1
                count += 1
    print(count)