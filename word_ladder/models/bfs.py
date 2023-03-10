import logging
from collections import deque


class BFS:
    """
    Class which represents a BFS algorithm.

    :param start_word: input str, the start point of a chain
    :param end_word: input str, the finish point of a chain
    :param dictionary: a graph of words already connected with each other
    :param queue: a queue for future visit vertices
    :param visited: a dict of visited vertices paired with vertex from which the first was visited
    """
    def __init__(self, start_word: str, end_word: str, dictionary: dict) -> None:
        self.start_word = start_word
        self.end_word = end_word
        self.dictionary = dictionary
        self.queue = deque([self.start_word])
        self.visited = {self.start_word: None}

    def make_path(self) -> list:
        """
        Analyze of the visited dictionary.
        If end_word not in visited, the exception will be raised.
        1. Starting from the end_word, look up the visited dictionary for the next path vertex.
        2. Adding current vertex to result list.
        3. The following steps will repeat until current vertex will be equal start_word.

        :return: a result list containing a chain from start_word to end_word
        """
        if self.end_word not in self.visited:
            logging.error("End word has no connection to Start word!")
            raise Exception("End word has no connection to Start word!")
        logging.info("Path found. Analyzing...")
        result = [self.end_word]
        current_vertex = self.end_word
        while current_vertex != self.start_word:
            current_vertex = self.visited[current_vertex]
            result.append(current_vertex)
        return list(reversed(result))

    def search(self) -> list:
        """
        The algorithm of search itself.
        1. Takes the first element from a queue, checks if it's end_word.
        2. Takes the edges of a current vertex, checks if they are already visited.
        3. If not - adds to queue, marks as visited paired with the current vertex.
        4. The following steps will repeat until the current vertex equals end_word or the queue becomes empty.

        :return: a result list with a chain from start_word to end_word
        """
        while self.queue:
            current_vertex = self.queue.popleft()
            if current_vertex == self.end_word:
                break

            next_vertices = self.dictionary[current_vertex]
            for next_vertex in next_vertices:
                if next_vertex not in self.visited:
                    self.queue.append(next_vertex)
                    self.visited[next_vertex] = current_vertex
        return self.make_path()
