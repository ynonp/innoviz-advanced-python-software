# Implement the function group by so it will:
# call key_function on each element in stuff
# return a dictionary, where:
#   key is the result of key_function
#   value is a list of the values for which key_function(x) === key

from typing import TypeVar, Dict, Callable, List
from collections import defaultdict

# Generics (Type Var)
T = TypeVar('T')
K = TypeVar('K')

# Please type "2" in the chat when it's ready
def groupby(key_function: Callable[[T], K], *stuff: T) -> Dict[K, List[T]]:
    result = defaultdict(list)

    for item in stuff:
        result[key_function(item)].append(item)

    return result



# returns: { h: ['hello', 'hi', 'help', 'here'], b: ['bye'] }
res = groupby(lambda s: s[0], 'hello', 'hi', 'help', 'bye', 'here')
print(res)
