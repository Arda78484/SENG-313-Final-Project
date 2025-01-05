def lcs_optimized(str1, str2):
    m, n = len(str1), len(str2)
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    # Build the DP table using two rows
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, prev

    lcs_length = prev[-1]

    # Backtracking to find one LCS
    def backtrack():
        i, j = m, n
        result = []
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                result.append(str1[i - 1])
                i -= 1
                j -= 1
            elif prev[j] == prev[j - 1]:
                j -= 1
            else:
                i -= 1
        return ''.join(reversed(result))

    lcs_string = backtrack()
    return lcs_length, lcs_string

if __name__ == "__main__":
    # Read the two documents
    with open(r"documents\\doc1.txt", "r", encoding="utf-8") as file1:
        text1 = file1.read()

    with open(r"documents\\doc2.txt", "r", encoding="utf-8") as file2:
        text2 = file2.read()

    # Compute LCS
    length, lcs_string = lcs_optimized(text1, text2)

    # Output the results
    print(f"Length of Longest Common Subsequence: {length}")
    print(f"Longest Common Subsequence: {lcs_string}")
