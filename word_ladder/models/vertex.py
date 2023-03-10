class Vertex:
    """
    The class which refers to a vertex of a graph.

    :param data: attribute stands for a word itself
    :param edges: a list of vertices(words) which differ by one letter
    """
    def __init__(self, data: str) -> None:
        self.data = data
        self.edges = list()

    def __str__(self) -> str:
        return f"{self.data}->{'->'.join([vertex.data for vertex in self.edges])}"

    def is_match(self, compared_vertex) -> bool:
        """
        Checks if words differ by only one letter.
        Look up of the letters of both vertices simultaneously. If their characters difference equals one - match.

        :param compared_vertex: a compared Vertex object
        :return: bool, if words match - their differ is one character
        """
        return sum([char1 != char2 for char1, char2 in zip(self.data, compared_vertex.data)]) == 1
