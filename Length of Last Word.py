def lengthOfLastWord(s):
    a = s.split()
    return len(a[-1])



s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))