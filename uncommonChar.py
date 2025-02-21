def uncommonChars(self, s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    unique_chars = set1.symmetric_difference(set2)
    result = ''.join(sorted(unique_chars))
    return result