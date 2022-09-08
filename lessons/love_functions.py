"""Some tender, loving functions."""

from importlib.util import spec_from_loader


def love(subject: str) -> str:
    """Given a subject as a parameter, return a loving string."""
    return f"I love you {subject}!"

def spread_love(to: str, n: int) -> str:
    """Generates a str repeating a loving message n times"""
    love_note = ""
    i: int = 0
    while i < n:
        i += 1
        love_note += love(to) + "\n"
    return love_note
