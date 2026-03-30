def word_count_dict(sentences):
    count = {}

    for sentence in sentences:
        for word in sentence:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

    return count