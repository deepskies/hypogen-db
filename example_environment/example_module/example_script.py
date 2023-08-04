from datetime import datetime

"""
Some mock functions with basic type annotations and docstrings.
"""
def return_current_date() -> datetime:
    """
    Returns the current date and time stamp.

    Returns:
        A date-time time stamp in UTC.
    """
    return datetime.now()

def guess_methuselah_age(hypothesis: int, excess_argument: str = None) -> str:
    """
    Evaluates whether a user has entered the correct age of Methuselah.

    Args:
        hypothesis: An integer representing the user's guess of mMthuselah's age.
    Returns:
        Returns a string that lets the user know whether they've guessed correctly.
    Raises:
        ValueError: the integer guess is too low to be serious.

    Examples:
        >>> guess_methuselah_age(hypothesis=1000)
        >>> guess_methuselah_age(hypothesis=100, excess_argument = "cowa-bunga, dude!")
    """
    if hypothesis <= 100:
        raise ValueError("Very funny, but you know that age range is not correct.")
    elif hypothesis == 969:
        return "Woah, how'd you know that very specific piece of information?"
    else:
        return "Not quite, but try again!"