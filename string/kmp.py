def find_LPS(pattern):
    n = len(pattern)
    lps = [0] * n

    l = 0
    i = 1
    while i < n:
        if pattern[i] == pattern[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l == 0:
                lps[i] = 0
                i += 1
            else:
                l = lps[l-1]
    return lps

def kmp(T, P):
    n, m = len(T), len(P)
    position = []
    lps = find_LPS(P)

    i = 0
    j = 0
    while i < n:
        if T[i] == P[j]:
            i += 1
            j += 1
            if j == m:
                position.append(i-j)
                j = lps[j-1]
        else:
            if j:
                j = lps[j-1]
            else:
                i += 1
                
    return position

# test case 1
T = "As you expect, this text 'T' is just a simple example text. So this text dose not have any meaning."
P = "text"

pattern_index = kmp(T, P)
print(*pattern_index)
# output : 20 54 68