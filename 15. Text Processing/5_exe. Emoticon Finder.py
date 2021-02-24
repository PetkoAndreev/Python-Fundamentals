emoticons = input()

for i in range(len(emoticons)):
    if emoticons[i] == ':':
        print(emoticons[i] + emoticons[i+1])