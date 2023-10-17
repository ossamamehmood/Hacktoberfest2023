def sierpinski(n,tab, pattern_length):
    """Returns a list of lists of strings representing a Sierpinski triangle
       see : https://en.wikipedia.org/wiki/Sierpiński_triangle
    """
    if n == 1:
      return tab
    temp = [i[:] for i in tab]
    for i in range(len(temp)):
        tab[i] *= 2
        tab.append(temp[i])
        for _ in range(len(tab[0])-len(temp[i])):
            temp[i].append(' ' * pattern_length)
    return sierpinski(n//2,tab, pattern_length)

def print_sierpinski(tab):
    """Prints a Sierpinski triangle"""
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print(tab[i][j], end='')
        print(end = "\n")

if __name__ == '__main__':
    # example use case
    pattern = [["Remi"]]
    length = len(pattern[0][0])
    result = sierpinski(56, pattern, length)
    print_sierpinski(result)
