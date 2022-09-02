string = "I am a teacher and I love to inspire and teach people"
Words_string = string.split(" ")
counts = dict()
unique_Words = []
for word in Words_string:
    if word in unique_Words:
        counts[word] += 1
    else:
        counts[word] = 1
print(len(counts))