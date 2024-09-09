"""adfghk."""


def check_first_letter(word: str, letter: str) -> str:
    """writing a fucntion to see if the first letter matches  the word."""
    if word[0] == letter:
        return "match"
    else:
        return "no match"


print(check_first_letter("hello", "e"))
