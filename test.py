def anagrams(s1, s2):
    ## replace the 'pass' command (which does nothing) with code that
    ## computes and returns the requried result for any strings s1 and s2
    s1Count = [0 for _ in range(26)]
    s2Count = [0 for _ in range(26)]
    if (s1 == s2 or len(s1) != len(s2)):
        return False
    for i in range(len(s1)):
        if ord(s1[i] < 97):
            s1Count[ord(s1[i] - 65)] += 1
        else:
            s1Count[ord(s1[i] - 97)] += 1
        if ord(s2[i] < 97):
            s2Count[ord(s1[i] - 65)] += 1
        else:
            s2Count[ord(s1[i] - 97)] += 1
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            return False
    return True
