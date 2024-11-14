def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    filtered_paragraph = "".join([c if c.isalpha() or c.isspace() else " " for c in paragraph.lower()])

    words = filtered_paragraph.split(" ")

    banned_set = set(banned)

    valid_words = [word for word in words if word not in banned_set and word != ""]

    counts = {}

    for word in valid_words:
        counts[word] = counts.get(word, 0) + 1

    max_word = max(counts, key=counts.get)

    return max_word