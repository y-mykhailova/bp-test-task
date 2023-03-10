import pytest

from .constants import (
    DICTIONARY_WORDS,
    GRAPH_DICTIONARY_ONE_WORD,
    GRAPH_DICTIONARY_TWO_UNCONNECTED_WORDS,
    GRAPH_DICTIONARY_FIVE_WORDS,
    GRAPH_DICTIONARY_MANY_WORDS,
)
from .fixtures import graph_object


@pytest.mark.parametrize(
    "graph_object, expected",
    [
        ([DICTIONARY_WORDS[0]], GRAPH_DICTIONARY_ONE_WORD),
        (
            [DICTIONARY_WORDS[0], DICTIONARY_WORDS[-3]],
            GRAPH_DICTIONARY_TWO_UNCONNECTED_WORDS,
        ),
        (DICTIONARY_WORDS[0:5], GRAPH_DICTIONARY_FIVE_WORDS),
        (DICTIONARY_WORDS[0:-2], GRAPH_DICTIONARY_MANY_WORDS),
    ],
    indirect=["graph_object"],
)
def test_creation_of_graph(graph_object, expected):
    assert graph_object.to_dict() == expected


@pytest.mark.parametrize(
    "graph_object",
    [
        DICTIONARY_WORDS,
    ],
    indirect=["graph_object"],
)
def test_validation_on_dictionary_words_length(graph_object):
    assert len(graph_object.vertices) == 10
