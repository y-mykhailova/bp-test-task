import logging

from word_ladder.models.bfs import BFS
from word_ladder.models.graph import Graph


def read_file(dictionary_file: str) -> list:
    """
    Reads the dictionary file.
    Raises an exception if file does not exist.

    :param dictionary_file: the name of read file
    :return: list[str] of words
    """
    try:
        with open(dictionary_file) as file:
            return [line.strip() for line in file]
    except FileNotFoundError as e:
        logging.error("The entered dictionary file does not exist")
        raise Exception("The entered dictionary file does not exist") from e


def validate_start_end_words(start_word: str, end_word: str, words: list) -> None:
    """
    Validator for input data.
    Checks if the start_word and end_word are 4-letter and present in a dictionary_file.
    Raises an exception in case of failure.

    :param start_word: input str, the start point of a chain
    :param end_word: input str, the finish point of a chain
    :param words: a list of words from input dictionary file
    :return: None
    """
    if len(start_word) != 4 or len(end_word) != 4:
        logging.error("Start and end word's length should be 4")
        raise ValueError("Start and end word's length should be 4")
    if start_word not in words or end_word not in words:
        logging.error("Start or end word is not presented in the dictionary file")
        raise ValueError("Start or end word is not presented in the dictionary file")


def write_to_file(result_file: str, result: list) -> None:
    """
    Write to result file the calculated chain from start_word to end_word.

    :param result_file: the name of result file, where the chain will be written
    :param result: a list of words calculated from start_word to end_word
    :return: None
    """
    with open(result_file, "w") as file:
        file.write("\n".join(result))


def main():
    """
    The entrypoint for word-ladder - calculating the path from start_word to end_word
    which differ by one letter.
    """
    logging.basicConfig(
        filename="log.txt", format="%(asctime)s %(message)s", level=logging.INFO
    )
    logging.info("New session started")

    dictionary_file = (
            input("Enter the name of dictionary file (def: dictionary.txt)-> ")
            or "dictionary.txt"
    )
    start_word = input("Enter the start word -> ")
    end_word = input("Enter the end word -> ")
    result_file = (
            input("Enter the name of result file (def: result.txt)-> ") or "result.txt"
    )

    words = read_file(dictionary_file)
    validate_start_end_words(start_word, end_word, words)

    graph = Graph()
    graph.insert_list(words)

    bfs = BFS(start_word, end_word, graph.to_dict())
    result = bfs.search()
    write_to_file(result_file, result)
    logging.info(f"Successfully wrote the result to file {result_file}")
    logging.info("Session finished\n")


if __name__ == "__main__":
    main()
