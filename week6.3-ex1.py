from typing import List


def words_length(sentence: str) -> List[int]:
    """
    The function receives a sentence and returns the length of each word in it, in the order received.
    :param sentence: The statement that the function checks.
    :return: List of word lengths in a sentence.
    """
    return [len(word) for word in sentence.split(" ")]


if __name__ == '__main__':
    print(words_length("Toto, I've a feeling we're not in Kansas anymore"))
