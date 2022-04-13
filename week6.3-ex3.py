TEXT = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""


def count_words(text_to_check: str) -> dict:
    """
    The function receives text and checks the length of each word in it.
    :param text_to_check: The text that is examined is the length of each word in it.
    :return: A dictionary where the key is the name of the word and the value is its length.
    """
    text_to_check = (''.join(char.lower() for char in text_to_check.replace('\n', ' ') if char.isalpha() or ' '))\
        .split(' ')
    return {text_to_check[index]: len(text_to_check[index]) for index in range(len(text_to_check))
            if text_to_check[index].isalpha()}


if __name__ == '__main__':
    print(count_words(TEXT))
