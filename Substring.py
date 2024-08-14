def generate_substrings(s):
    substrings = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 1, length + 1):
            substrings.add(s[i:j])
    return substrings


substrings1 = generate_substrings("ABC")
substrings2 = generate_substrings("ACB")

print(substrings1)
print(substrings2)
common_substrings = substrings1.intersection(substrings2)
print(common_substrings)

max_length = 0
for substring in common_substrings:
    if len(substring) > max_length:
        max_length = len(substring)

print(max_length)
