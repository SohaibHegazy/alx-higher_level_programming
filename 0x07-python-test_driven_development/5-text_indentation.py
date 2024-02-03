#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """prints a text with 2 new lines after ., ? and :

    Args:
    text: the text

    Raise:
    TypeError("text must be a string") if text is not a string

    Return:
    print the passed text with 2 lines after ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for ch in ".?:":
        # print(ch, text.split(ch))
        text = (ch + "\n\n").join(
            [line.strip(" ") for line in text.split(ch)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
