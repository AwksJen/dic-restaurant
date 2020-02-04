words = {}

def word_count(file):
    file = open(file)
    for line in file:
        if len(line) > 10:
            line = line.strip()
            line = line.split(':')
            words[line[0]] = line[1]
    for key in sorted(words):
        print(f"{key} is rated at {words[key]}")
print(word_count('scores.txt'))
