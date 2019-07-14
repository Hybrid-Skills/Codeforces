q = int(input())

for _ in range(q):
    s = input()
    t = input()
    p = input()
    flag = True

    dictionary_s = {'a': 0, 'b': 0, 'c': 0,
                    'd': 0, 'e': 0, 'f': 0,
                    'g': 0, 'h': 0, 'i': 0,
                    'j': 0, 'k': 0, 'l': 0,
                    'm': 0, 'n': 0, 'o': 0,
                    'p': 0, 'q': 0, 'r': 0,
                    's': 0, 't': 0, 'u': 0,
                    'v': 0, 'w': 0, 'x': 0,
                    'y': 0, 'z': 0}

    dictionary_t = {'a': 0, 'b': 0, 'c': 0,
                    'd': 0, 'e': 0, 'f': 0,
                    'g': 0, 'h': 0, 'i': 0,
                    'j': 0, 'k': 0, 'l': 0,
                    'm': 0, 'n': 0, 'o': 0,
                    'p': 0, 'q': 0, 'r': 0,
                    's': 0, 't': 0, 'u': 0,
                    'v': 0, 'w': 0, 'x': 0,
                    'y': 0, 'z': 0}

    dictionary_p = {'a': 0, 'b': 0, 'c': 0,
                    'd': 0, 'e': 0, 'f': 0,
                    'g': 0, 'h': 0, 'i': 0,
                    'j': 0, 'k': 0, 'l': 0,
                    'm': 0, 'n': 0, 'o': 0,
                    'p': 0, 'q': 0, 'r': 0,
                    's': 0, 't': 0, 'u': 0,
                    'v': 0, 'w': 0, 'x': 0,
                    'y': 0, 'z': 0}

    for i in s:
        dictionary_s[i] += 1
    for i in p:
        dictionary_p[i] += 1
    for i in t:
        dictionary_t[i] += 1

    for i in range(26):
        char = chr(97 + i)
        if dictionary_t[chr(97+i)] > dictionary_s[chr(97+i)] + \
                dictionary_p[chr(97+i)]:
            print('no')
            flag = False
            break

    start = -1
    if flag:
        for i in s:
            try:
                start = t[start + 1:].index(i) + start + 1
            except ValueError:
                print('no')
                flag = False
                break

    if flag:
        print('yes')
