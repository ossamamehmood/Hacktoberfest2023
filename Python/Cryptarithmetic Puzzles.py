from itertools import permutations

def solve_cryptarithmetic(puzzle):
    # Split the puzzle into words and the result
    words = puzzle.split()[:-2]
    result_word = puzzle.split()[-1]

    # Generate all possible permutations of the digits 0-9
    digit_permutations = permutations('0123456789', len(set("".join(words + [result_word]))))

    for perm in digit_permutations:
        digit_mapping = dict(zip(set("".join(words + [result_word])), perm))
        if all(digit_mapping[word[0]] != '0' for word in words + [result_word]):
            # Replace letters with their corresponding digits and evaluate the expression
            expression = "".join([digit_mapping[char] for char in puzzle])
            if eval(expression):
                return digit_mapping
    return None

# Example usage
puzzle = "SEND + MORE = MONEY"
solution = solve_cryptarithmetic(puzzle)

if solution:
    print("Solution found:")
    for word in puzzle.split():
        print(word, "=>", "".join(solution[char] for char in word))
else:
    print("No solution found.")
