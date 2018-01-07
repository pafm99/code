# replace test-file.tx with text file with the file you want to evaluate

counts = {
    'lines': 0,
    'characters': 0,
    'words': 0
}
unique_words = set()

for counts['lines'], line in enumerate(open('test-file.txt'), 1):
    counts['characters'] += len(line)

    words = line.split()

    counts['words'] += len(words)
    unique_words.update(words)

counts['unique_words'] = len(unique_words)
for key, value in counts.items():
    print("{}: {}".format(key, value))
