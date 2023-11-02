def find_longest_substring(string):
    n = len(string)
    table = [[0] * (n+1) for _ in range(n+1)]
    longest_length = 0
    longest_end = 0

    for i in range(n):
        for j in range(n):
            if string[i] == string[n-1-j]:
                length = table[i][j] + 1
                table[i+1][j+1] = length
                if length > longest_length:
                    longest_length = length
                    longest_end = i

    longest_start = longest_end - longest_length + 1
    longest_substring = string[longest_start:longest_end+1]
    return longest_substring

# Example usage
string = "abcddcba"
longest_substring = find_longest_substring(string)

print("Longest Common Substring:", longest_substring)

