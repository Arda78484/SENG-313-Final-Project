def longest_common_subsequence(str1, str2):
    """
    Finds the Longest Common Subsequence (LCS) between two strings.

    :param str1: First string
    :param str2: Second string
    :return: Length of LCS and one possible LCS
    """
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find one LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], ''.join(reversed(lcs))

# Example test cases
def test_lcs():
    test_cases = [
        ("AGGTAB", "GXTXAYB"),
        ("ABCBDAB", "BDCABC"),
        ("XMJYAUZ", "MZJAWXU"),
    ]

    for i, (str1, str2) in enumerate(test_cases):
        length, lcs = longest_common_subsequence(str1, str2)
        print(f"Test Case {i + 1}:")
        print(f"String 1: {str1}")
        print(f"String 2: {str2}")
        print(f"LCS Length: {length}")
        print(f"LCS: {lcs}\n")

if __name__ == "__main__":
    test_lcs()