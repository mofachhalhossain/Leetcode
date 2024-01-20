def strStr(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1





haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))