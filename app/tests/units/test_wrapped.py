import pytest
from app.data.wrapped_extractor import parse_wrapped


@pytest.fixture
def wrapped_db_wrapped():
    return {'title': 'Michael Jordan', 'summary': 'Michael J does a backflip!',
            'image': '/kjhLKFIUGichaeIADSp.jpg', 'popularity': 7}


def test_parse_wrapped(wrapped_db_wrapped):
    wrapped = parse_wrapped(wrapped_db_wrapped)
    assert wrapped.title == wrapped_db_wrapped['title']
    assert wrapped.summary == wrapped_db_wrapped['summary']
    assert wrapped.image == wrapped_db_wrapped['image']
    assert wrapped.popularity == wrapped_db_wrapped['popularity']
