
# def longest_substring(s):
#
#     l = 0
#     longest_length = 0
#     substring_set = set()
#
#     for r in range(len(s)):
#         if s[r] in substring_set:
#             substring_set.remove(s[r])
#             l += 1
#
#         else:
#             substring_set.add(s[r])
#             if longest_length < (r - l) + 1:
#                 longest_length = (r - l) + 1
#
#         print(substring_set, longest_length)
#
#     return longest_length
#
# print(longest_substring("abcabcbb"))

# def max_average(nums, k):
#
#     current_sum = 0
#
#     for x in range(k):
#         current_sum += nums[x]
#
#     maximum_avg = current_sum / k
#
#     for y in range(k, len(nums)):
#         current_sum += nums[y]
#         current_sum -= nums[y - k]
#
#         maximum_avg = max(maximum_avg, current_sum / k)
#
#
#     return maximum_avg
#
# print(max_average([1,12,-5,-6,50,3], 4))


def smallest_subarray(nums, target):

    sml_subarray = float('inf')
    left = 0
    right = 0
    exists = False

    while right < len(nums):
        count = len(nums[left:right])
        sum_subarray = sum(nums[left:right])

        if sum_subarray >= target:
            if count < sml_subarray:
                sml_subarray = count
            left += 1
            exists = True
        else:
            right += 1

    if exists:
        return sml_subarray
    return False

print(smallest_subarray([1, 1, 1, 1, 1], 7))

