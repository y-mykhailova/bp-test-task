import pytest

from .constants import (
    BFS_DICTIONARY_ONE_WORD,
    BFS_1_DICTIONARY_FIVE_WORDS,
    BFS_2_DICTIONARY_FIVE_WORDS,
    BFS_1_DICTIONARY_MANY_WORDS,
    BFS_2_DICTIONARY_MANY_WORDS,
    BFS_3_DICTIONARY_MANY_WORDS,
)
from .fixtures import (
    make_bfs_object_unconnected_graph,
    make_bfs_object_one_vertex_graph,
    make_bfs_object,
)


def test_bfs_algorithm_one_vertex_graph(make_bfs_object_one_vertex_graph):
    result = make_bfs_object_one_vertex_graph.search()
    assert result == BFS_DICTIONARY_ONE_WORD


def test_bfs_algorithm_unconnected_graph(make_bfs_object_unconnected_graph):
    with pytest.raises(Exception, match="End word has no connection to Start word!"):
        make_bfs_object_unconnected_graph.search()


@pytest.mark.parametrize(
    "make_bfs_object, expected",
    [
        (BFS_1_DICTIONARY_FIVE_WORDS, BFS_1_DICTIONARY_FIVE_WORDS[1][1]),
        (BFS_2_DICTIONARY_FIVE_WORDS, BFS_2_DICTIONARY_FIVE_WORDS[1][1]),
        (BFS_1_DICTIONARY_MANY_WORDS, BFS_1_DICTIONARY_MANY_WORDS[1][1]),
        (BFS_2_DICTIONARY_MANY_WORDS, BFS_2_DICTIONARY_MANY_WORDS[1][1]),
        (BFS_3_DICTIONARY_MANY_WORDS, BFS_3_DICTIONARY_MANY_WORDS[1][1]),
    ],
    indirect=["make_bfs_object"],
)
def test_bfs_algorithm_simple_complex_graphs(make_bfs_object, expected):
    result = make_bfs_object.search()
    assert result == expected
