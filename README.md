# Word Ladder
The **goal** of the task is to build an application to calculate the shortest list of four-letter words with the following parameters:
- *dictionary_file* - the file name or path, containing four-letter words;
- *start_word* - a four-letter word from which to start a path (must be presented in a *dictionary_file*);
- *end_word* - a four-letter word, destination (must be presented in a dictionary_file);
- *result_file* - the file name or path, containing the shortest path from *start_word* to *end_word*.
***
### Run commands
There's no need-to-install depedencies for running the application. Otherwise, they will be in *requirements.txt* file.\
To run use:
```
python word_ladder/main.py
```
Also *setuptools* can be used for starting the application. To run the application, go to folder with *setup.py* file and run
the following command:
```
pip install .
```
After that the application can be run from the terminal with the following command:
```
word_ladder
```
***
### Running included tests
To run implemented tests create a virtual environment, activate it, install the *requirements.dev.txt* and run.\
(Ex: *venv*):
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.dev.txt
pytest -s tests/
```
***
### Stages of implementation:
- [x] Implementing the required models for raw data processing (classes: Vertex, Graph);
- [x] Reading from file, processing data;
- [x] Implementing the BFS class with the corresponding algorithm and writing the result path to file;
- [x] Test development;
- [x] Adding logging to file *log.txt*;
- [x] Adding *setuptools* for terminal launching.
***
### Code structure and explanations to chosen implementation
Application project consists of 2 packages(*models* and *tests*) and running file(*main.py*)\
Package *models* refers to 3 main classes:
- **Vertex** - an object, simply a word which has a *data* - the actual word and a list of *edges* - words which differ from it with one letter;
- **Graph** - an object which represents a list of Vertices above. In current implementation Graph is unweighted and undirected;
- **BFS** - represents a BFS algorithm including *start_word*, *end_word*, *dictionary*, *queue* - vertices which need to be visited, *visited* - visited vertices excluded from a queue.

Breadth-first search (BFS) is an algorithm used for traversing a graph data structure. It starts at a given vertex and explores all the vertices at the current level before moving to the next level. In an unweighted undirected graph, the BFS algorithm can be implemented as follows:

1. Choose a starting vertex and mark it as visited.
2. Add the starting vertex to a queue.
3. While the queue is not empty, do the following:
   - Dequeue a vertex from the queue and print it.
   - For each adjacent vertex of the dequeued vertex, if it has not been visited yet, mark it as visited and enqueue it.
4. Repeat step 3 until the queue is empty.

Implementation also contains 12 tests, developed with pytest.
***
### Assumptions
- Given dictionary file with words is \n separated list of words;
- Given words from dictionary file may be longer or shorter than 4 letters, but they will be skipped;
- The application is case-sensitive: Spin != spin;
- The name of input and output files should be provided with the extension *.txt*;
- In case of giving wrong data (start_word or end_word is not in input file) the exception will be raised;
- Dictionary file contains unique words: Spin != Spin;
- Logs are stored in *log.txt*.