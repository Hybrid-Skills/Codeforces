# Methodius received an email from his friend Polycarp. However,
# Polycarp's keyboard is broken, so pressing a key on it once may
# cause the corresponding symbol to appear more than once (if you
# press a key on a regular keyboard, it prints exactly one symbol).
#
# For example, as a result of typing the word "hello", the following
# words could be printed: "hello", "hhhhello", "hheeeellllooo", but
# the following could not be printed: "hell", "helo", "hhllllooo".
#
# Note, that when you press a key, the corresponding symbol must
# appear (possibly, more than once).
#
# For each word in the letter, Methodius has guessed what word
# Polycarp actually wanted to write, but he is not sure about it,
# so he asks you to help him.
#
# You are given a list of pairs of words. For each pair, determine
# if the second word could be printed by typing the first one on
# Polycarp's keyboard.


def check_possible(original, typed):
    j = 0
    for char in typed:
        try:
            if char == original[j]:
                j += 1
        except IndexError:
            pass
        if char == original[abs(j-1)]:
            pass
        else:
            return 'NO'
    else:
        if j == len(original):
            return 'YES'
        else:
            return 'NO'


n = int(input())
for _ in range(n):
    original1 = input()
    typed1 = input()
    print(check_possible(original1, typed1))
