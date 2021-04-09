dictionary = set()
li = set()
lis = set()


def read_dictionary_file():
    global dictionary
    global contents

    with open("list.txt", "r", encoding='utf-8') as f:
        contents = f.read()
    dictionary = set(
        word
        for word in contents.splitlines()
    )


def is_banan_correctly(word):
    read_dictionary_file()
    return word in dictionary


def suggested_word(word):
    global sc
    max_s = 10000
    global te
    global li
    global lis
    global source
    te = word

    for sug in contents.splitlines():
        so = sug
        source_value = minimum_distance(so, te)
        if source_value <= max_s:
            max_s = source_value
            source = so
        final_value = max_s
        li = set()
    for sug in contents.splitlines():
        so = sug
        source_value = minimum_distance(so, te)
        if source_value == final_value:
            li.add(so)
            # lis = lis.union(li)
    return li


def minimum_distance(s, t):
    s = ' ' + s
    t = ' ' + t
    d = {}
    S = len(s)
    T = len(t)
    for i in range(S):
        d[i, 0] = i
    for j in range(T):
        d[0, j] = j
    for j in range(1, T):
        for i in range(1, S):
            if s[i] == t[j]:
                d[i, j] = d[i - 1, j - 1]
            else:
                d[i, j] = min(d[i - 1, j], d[i, j - 1], d[i - 1, j - 1]) + 1
    return d[S - 1, T - 1]


values = input()
for value in values.split(" "):
    if not is_banan_correctly(value):
        print("Spelling error: " + value)
        print("Suggested word: " + str(suggested_word(value)))

    else:
        print("Correct!")




