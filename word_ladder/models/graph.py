import logging

from .vertex import Vertex


class Graph:
    """
    A class which represents a graph.

    :param vertices: a list of Vertex objects(words)
    """
    def __init__(self) -> None:
        self.vertices = list()

    def __str__(self) -> str:
        return "\n".join(str(vertex) for vertex in self.vertices)

    def to_dict(self) -> dict:
        """
        Returns a dictionary of vertices of graph in a format appropriate for later algorithm run.

        :return: a dict with Vertex objects
        """
        return {
            vertex.data: ([child_vertex.data for child_vertex in vertex.edges])
            for vertex in self.vertices
        }

    def make_connections(self, new_vertex: Vertex) -> None:
        """
        Makes a connection of a created vertex to other vertices in a graph.
        If a new vertex differs from a vertex in a graph by one letter - add to edges list of both.

        :param new_vertex: a Vertex object which is going to be added
        :return: None
        """
        for vertex in self.vertices:
            if new_vertex.is_match(vertex):
                new_vertex.edges.append(vertex)
                vertex.edges.append(new_vertex)

    def insert(self, word: str) -> None:
        """
        Created new Vertex object, makes connections, adds vertex to vertices of graph.

        :param word: input word from dictionary file which is going to be added
        :return: None
        """
        new_vertex = Vertex(word)
        self.make_connections(new_vertex)
        self.vertices.append(new_vertex)

    def insert_list(self, words: list) -> None:
        """
        Processing a list of words from dictionary file. Adding to the graph.
        If a word contains more or less letters - the word will be skipped.

        :param words: a list of words from dictionary file
        :return: None
        """
        for word in words:
            if len(word) != 4:
                logging.warning(f"Skipping non-4-letter word - {word}")
            else:
                self.insert(word)
