def find_5_words(index: int):
    global counter, fruit
    if index >= 5:
        return [""]

    for i in range(len(words)):
        new = []
        for char, n in zip(words[i], board[index]):
            if fruit.get(char, counter) == n:
                if n == counter:
                    fruit[char] = counter
                    counter += 1
                    new.append(char)
            else:
                for char in new:
                    del fruit[char]
                    counter -= 1
                break
        else:
            if solution := find_5_words(index + 1):
                return [words[i]] + solution

            for char in new:
                del fruit[char]
                counter -= 1

    return []


board = [
    [0, 1, 2, 3, 4],
    [2, 5, 6, 7, 3],
    [8, 4, 2, 5, 7],
    [9, 2, 1, 8, 9],
    [7, 9, 3, 7, 8],
]

with open("words.txt") as f:
    words = f.read().splitlines()

fruit = {}
counter = 0
print(" ".join(find_5_words(0)))
