"""
    You are given two strings word1 and word2.
    Merge the strings by adding letters in alternating order,
    starting with word1. 
    If a string is longer than the other,
    append the additional letters onto the end of the merged string.
    Return the merged string.
"""

def mergeAlternately(word1: str, word2: str) -> str:
    A , B = len(word1), len(word2)
    merged = []
    a, b = 0, 0
    word = 1

    while a < A and b < B:
        if word == 1:
            merged.append(word1[a])
            a += 1
            word = 2
        if word == 2:
            merged.append(word2[b])
            b += 1
            word = 1
    
    if a < A:
        merged.append(word1[a])
        a += 1
    if b < B:
        merged.append(word2[b])
        b += 1
    return ''.join(merged)



# Test cases  
if __name__ == "__main__":
    # Test cases
    print(mergeAlternately("abc", "pqr"))  # Output: "apbqcr"
    print(mergeAlternately("ab", "pqrs"))  # Output: "apbqrs"
    print(mergeAlternately("abcd", "pq"))  # Output: "apbqcd"
    print(mergeAlternately("", ""))         # Output: ""
    print(mergeAlternately("a", ""))        # Output: "a"
    print(mergeAlternately("", "b"))        # Output: "b"
    print(mergeAlternately("abc", "defgh")) # Output: "adbecfgh"
    print(mergeAlternately("abcde", "123")) # Output: "a1b2cde"
    print(mergeAlternately("123", "abcde")) # Output: "1a2b3cde"
    print(mergeAlternately("abc", "def"))   # Output: "adbecf"
    print(mergeAlternately("abc", "d"))     # Output: "adb"
    print(mergeAlternately("a", "b"))       # Output: "ab"