same_vowel_end = 0
same_vowel = 0
question = []
vowels = 'aeiou'
vowel_question = []
vowel_question_end = []
last_vowel = '0'


n = int(input())
for _ in range(n):
    question.append(input())

for i in question:
    vowel = 0
    for j in i:
        if i in vowels:
            vowel += 1
            last_vowel = i
    vowel_question.append(vowel)
    vowel_question_end.append(last_vowel)

while n > 0:
    for k in range(1,n):
        if vowel_question[0] == vowel_question[k] and vowel_question_end[0] == vowel_question_end[k]:
            same_vowel += 1
            same_vowel_end += 1
        elif vowel_question[0] == vowel_question[k]:
            same_vowel += 1
    n -= 1
    del vowel_question[0]
    del vowel_question_end[0]

answer = same_vowel_end * (same_vowel - 1)

print(answer)