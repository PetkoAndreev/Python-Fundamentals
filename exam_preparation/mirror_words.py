import re

words = input()
words_data = []
mirror_words = []
pattern = r'(#|@)[a-zA-z]{3,}\1{2}[a-zA-Z]{3,}\1'
match_words = re.finditer(pattern, words)
for word in match_words:
    words_data.append(word.group().replace('@', '').replace('#', ''))

if words_data == []:
    print('No word pairs found!')
else:
    print(f'{len(words_data)} word pairs found!')

for word in words_data:
    word1 = word[:len(word)//2]
    word2 = word[len(word)//2:]
    word2_rev = word2[-1::-1]
    if word1 == word2_rev:
        mirror_words.append(word1 + ' <=> ' + word2)

if mirror_words == []:
    print('No mirror words!')
else:
    print('The mirror words are:')
    print(', '.join(mirror_words))