from example_environment import __version__
from example_environment.example_module.example_script import (
    guess_methuselah_age, 
    return_current_date
)

import pytest 
from datetime import datetime

def test_version():
    assert __version__ == '0.1.0'


def test_return_current_date():
    # The time-traveller test 
    assert return_current_date().year == datetime.now().year

def test_guess_methuselah_age_success():
    
    assert ("Woah, how'd you know that very specific piece of information?" 
                == guess_methuselah_age(hypothesis=969)
                )

def test_guess_methuselah_age_fail():
    
    assert ("Not quite, but try again!" == guess_methuselah_age(hypothesis=1000))

def test_guess_methuselah_age_bad_guess():
    
    with pytest.raises(ValueError):
        guess_methuselah_age(hypothesis=1)

def test_get_some_data(example_fixture_data):
    # Uses the fixture data from conftest.py
    assert 'age' in  example_fixture_data.keys()
    assert "favorite_movie" in example_fixture_data.keys()