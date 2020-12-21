def groupby(key_function, *stuff) -> dict:
    pass

# returns: { h: ['hello', 'hi', 'help', 'here'], b: ['bye'] }
groupby(lambda s: s[0], 'hello', 'hi', 'help', 'bye', 'here')

{
    'h': ['hello', 'hi', 'help', 'here'],
    'b': ['bye']
}
