# emojize.py

import emoji

inp = input("Input:")
emojized = emoji.emojize(inp, language='alias')
print(emojized)
