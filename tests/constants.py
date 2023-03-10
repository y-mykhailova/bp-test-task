DICTIONARY_WORDS = (
    "Spin",
    "Spit",
    "Spue",
    "Sput",
    "Spat",
    "Spul",
    "Spal",
    "Stat",
    "Stap",
    "Stop",
    "Spectacular",
    "Bicycle",
)
GRAPH_DICTIONARY_ONE_WORD = {
    "Spin": [],
}
GRAPH_DICTIONARY_TWO_UNCONNECTED_WORDS = {
    "Spin": [],
    "Stop": [],
}
GRAPH_DICTIONARY_FIVE_WORDS = {
    "Spin": ["Spit"],
    "Spit": ["Spin", "Sput", "Spat"],
    "Spue": ["Sput"],
    "Sput": ["Spit", "Spue", "Spat"],
    "Spat": ["Spit", "Sput"],
}
GRAPH_DICTIONARY_MANY_WORDS = {
    "Spin": ["Spit"],
    "Spit": ["Spin", "Sput", "Spat"],
    "Spue": ["Sput", "Spul"],
    "Sput": ["Spit", "Spue", "Spat", "Spul"],
    "Spat": ["Spit", "Sput", "Spal", "Stat"],
    "Spul": ["Spue", "Sput", "Spal"],
    "Spal": ["Spat", "Spul"],
    "Stat": ["Spat", "Stap"],
    "Stap": ["Stat", "Stop"],
    "Stop": ["Stap"],
}
BFS_DICTIONARY_ONE_WORD = ["Spin"]
BFS_1_DICTIONARY_FIVE_WORDS = [GRAPH_DICTIONARY_FIVE_WORDS], [
    ["Spin", "Spue"],
    ["Spin", "Spit", "Sput", "Spue"],
]
BFS_2_DICTIONARY_FIVE_WORDS = [GRAPH_DICTIONARY_FIVE_WORDS], [
    ["Spat", "Spin"],
    ["Spat", "Spit", "Spin"],
]
BFS_1_DICTIONARY_MANY_WORDS = [GRAPH_DICTIONARY_MANY_WORDS], [
    ["Spin", "Spal"],
    ["Spin", "Spit", "Spat", "Spal"],
]
BFS_2_DICTIONARY_MANY_WORDS = [GRAPH_DICTIONARY_MANY_WORDS], [
    ["Spin", "Spul"],
    ["Spin", "Spit", "Sput", "Spul"],
]
BFS_3_DICTIONARY_MANY_WORDS = [GRAPH_DICTIONARY_MANY_WORDS], [
    ["Stat", "Spul"],
    ["Stat", "Spat", "Sput", "Spul"],
]
