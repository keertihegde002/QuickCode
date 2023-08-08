"""
returns the lower INDEX value if the value is NOT PRESENT, otherwise INDEX
"""


def binarySearch(arr, l, r, x):
  
    while l <= r:
  
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
  
        else:
            r = mid - 1
    return l-1