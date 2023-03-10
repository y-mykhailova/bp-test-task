import pytest

from .constants import DICTIONARY_WORDS
from word_ladder.models.bfs import BFS
from word_ladder.models.graph import Graph


def make_graph(words: list) -> Graph:
    test_graph = Graph()
    test_graph.insert_list(words)
    return test_graph


@pytest.fixture
def graph_object(request) -> Graph:
    return make_graph(request.param)


@pytest.fixture
def make_bfs_object(request) -> BFS:
    tested_graph = make_graph(*request.param[0])
    bfs = BFS(request.param[1][0][0], request.param[1][0][1], tested_graph.to_dict())
    return bfs


@pytest.fixture
def make_bfs_object_one_vertex_graph() -> BFS:
    tested_graph = make_graph(DICTIONARY_WORDS[0])
    bfs = BFS(DICTIONARY_WORDS[0], DICTIONARY_WORDS[0], tested_graph.to_dict())
    return bfs


@pytest.fixture
def make_bfs_object_unconnected_graph() -> BFS:
    tested_graph = make_graph([DICTIONARY_WORDS[0], DICTIONARY_WORDS[-3]])
    bfs = BFS(
        DICTIONARY_WORDS[0],
        DICTIONARY_WORDS[-3],
        tested_graph.to_dict(),
    )
    return bfs
