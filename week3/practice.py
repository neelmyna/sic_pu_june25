import re

words = ["apple", "banana", "orange", "grape", "umbrella"]

# Capitalize if starts with a vowel
vowel_caps = list(map(lambda w: re.sub(r'^[aeiou]', lambda m: m.group(0).upper(), w), words))
print(vowel_caps)

# Capitalize the whole word if it starts with a vowel
vowel_caps = list(map(lambda w: re.sub(r'^[aeiou](\w+)', w.upper(), w), words))
print(vowel_caps)

# re.sub(r'[^a-zA-Z]
# lambda s: re.sub(r'[^a-zA-Z]', '', s