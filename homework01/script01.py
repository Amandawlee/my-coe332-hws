def longest(x):
    return len(x)

words = []
with open('/usr/share/dict/words', 'r') as f:
    words = f.read().splitlines()

words.sort(key=longest)

print(words[-5:])
