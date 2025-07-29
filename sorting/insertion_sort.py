from hamcrest import equal_to, assert_that


# Insertion sort
def insertion_sort(nums: list) -> list:
    for i in range(1, len(nums)):
        current_value = nums[i]
        j = i-1
        while j >= 0 and nums[j] > current_value:
            # This could have one less writing
            nums[j], nums[j+1] = current_value, nums[j]
            j -= 1
    print(nums)
    return nums

def optimal_insertion_sort(l: list):
    for n in range(1, len(l)):
        current_value = l[n]
        i=n-1
        while i >= 0 and current_value < l[i]:
            l[i+1] = l[i]
            i-=1
        l[i+1] = current_value 
    return l

            
def insertion_sort_reverse(nums: list) -> list:
    for i in range(1, len(nums)):
        current_value = nums[i]
        left = i-1
        while nums[left] < current_value and left >= 0:
            nums[left], nums[left+1] = current_value, nums[left]
            left -= 1
    print(nums)
    return nums



if __name__ == "__main__":
    assert_that(insertion_sort([5, 2, 4, 6, 1, 3]), equal_to([1, 2, 3, 4, 5, 6]))
    assert_that(insertion_sort([31, 41, 59, 26, 41, 58]), equal_to([26, 31, 41, 41, 58, 59]))    
    assert_that(optimal_insertion_sort([5, 2, 4, 6, 1, 3]), equal_to([1, 2, 3, 4, 5, 6]))
    assert_that(optimal_insertion_sort([31, 41, 59, 26, 41, 58]), equal_to([26, 31, 41, 41, 58, 59]))
    assert insertion_sort_reverse([5, 2, 4, 6, 1, 3]) == [6, 5, 4, 3, 2, 1]
    assert insertion_sort_reverse([31, 41, 59, 26, 41, 58]) == [59, 58, 41, 41, 31, 26]
