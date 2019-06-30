def isPalindrome(string):
    # Write your code here.
    if 0 == len(array) % 2:
        return False
    start = 0
    end = len(array) - 1

    while (start < end):
        if array[start] != array[end]:
            return False
        start = start + 1
        end = end - 1
    return True