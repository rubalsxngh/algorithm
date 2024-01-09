
def sorting(nums, st, en):
    high = nums[en]
    i = st-1

    for j in range(st, en):
        if nums[j] <= high:
            i += 1

            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[en] = nums[en], nums[i+1]
    return i+1


def quick(nums, st, en):
    if st < en:
        pivot = sorting(nums, st, en)
        quick(nums, st, pivot-1)
        quick(nums, pivot+1, en)
    
    return nums


def main():
    '''
        Sample input:
        Please enter the array (single-space-separated):
        100 60 70 80 30

        The sorted array is as follows: 30 60 70 80 100

    '''
    print("Please enter the array (single-space-separated):")
    nums = list(map(int, input().split()))

    sorted_arr = quick(nums, 0, len(nums) - 1)

    print("The sorted array is as follows:", sorted_arr)


if __name__ == '__main__':
    main()
