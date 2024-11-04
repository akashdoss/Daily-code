# Get input values
N, X, Y, Z = map(int, input().split())

# Initialize the sequence with the first three terms
sequence = [X, Y, Z]

# Generate terms from the 4th to the Nth term
for i in range(3, N):
    if i % 3 == 0:
        term = sequence[i - 3] + sequence[i - 2]
    elif i % 3 == 1:
        term = sequence[i - 2] + sequence[i - 1]
    else:
        term = sequence[i - 1] + sequence[i - 3]
    sequence.append(term)

# Print the first N terms in the sequence
print(*sequence)
