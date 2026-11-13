scores = [78, 92, 65, 88, 54, 99, 71]

for i in range(len(scores)):
    for j in range(len(scores)):
        if (scores[j] < scores[i]):
            scores[i], scores[j] = scores[j], scores[i]
print(scores)
print(scores[::-1])
print(scores[:3])