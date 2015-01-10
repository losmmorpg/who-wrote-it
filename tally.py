import string

# strip punctuation, make all lowercase
def undress_string(line):
    new = ""
    for c in line.lower():
        if c in (string.digits + string.ascii_lowercase + " "):
            new += c
    return new

def wordcount(source):
    try:
        count = 0
        for line in source:
            line = undress_string(line)
            for word in line.split(" "):
                if word != "":
                    count += 1
        return count
    except UnicodeDecodeError:
        #print("UnicodeDecodeError")
        return 0

# returns dict of word/count pairs for top-frequency words.
# max is limit of dict size, or 0 if full count should be included
def tally(source, max_count, top_words=None):
    try:
        counts = {}
        if top_words:
            for word in top_words:
                counts[word] = 1    # avoid 0 probabilities

        for line in source:
            line = undress_string(line)
            for word in line.split(" "):
                if word != "":
                    if word in (counts if not top_words else top_words):
                        counts[word] += 1
                    elif not top_words:
                        counts[word] = 1

        words = list(counts.items())
        return slice_top(words, max_count)
    except UnicodeDecodeError:
        #print("UnicodeDecodeError in", source)
        return {}

def slice_top(items, max_count):
    items.sort(key=lambda item: item[1])

    length = len(items) if max_count == 0 else min(len(items), max_count)
    return dict(items[-length:])

def merge_tallies(source, new, max_count):
    for word, count in new.items():
        if word in source:
            source[word] += count
        else:
            source[word] = count
    items = list(source.items())
    return slice_top(items, max_count)