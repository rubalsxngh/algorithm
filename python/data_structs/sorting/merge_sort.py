# Merge Sort Algorithm Explanation:
# Merge Sort is a divide-and-conquer sorting algorithm that works as follows:
# 1. Divide: The unsorted list is divided into n sub-lists, each containing one element.
# 2. Conquer: Adjacent sub-lists are repeatedly merged to produce new sorted sub-lists until there is only one sub-list remaining.
# 3. Combine: The final merged sub-list is the sorted output.

# The 'merge' function is responsible for merging two sorted halves of the array.
# The 'sorting' function is used to merge the divided sub-lists.

def sorting(nums, st, mid, en):
    # Merging two sorted sub-lists [st...mid] and [mid+1...en]
    id1, id2 = st, mid + 1
    new_arr = []

    while id1 <= mid and id2 <= en:
        if nums[id1] <= nums[id2]:
            new_arr.append(nums[id1])
            id1 += 1
        elif nums[id1] > nums[id2]:
            new_arr.append(nums[id2])
            id2 += 1

    while id1 <= mid:
        new_arr.append(nums[id1])
        id1 += 1

    while id2 <= en:
        new_arr.append(nums[id2])
        id2 += 1

    return new_arr


def merge(nums, st, en):
    if st < en:
        mid = (st + en) // 2

        merge(nums, st, mid)
        merge(nums, mid + 1, en)

        # Merge the sorted halves
        nums[st:en + 1] = sorting(nums, st, mid, en) 

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

    sorted_arr = merge(nums, 0, len(nums) - 1)

    print("The sorted array is as follows:", sorted_arr)

if __name__ == '__main__':
    main()
