word = "supercalifragilisticexpialidocious"
print(word[0])
print(word[2])

# variable[start:end:step]
print(word[0:5:1])
print(word[0:5:2])
print(word[5:9:1])
print(word[5:])
print(word[5::2])
print(word[:7])
print(word[:5])
print(word[::-1])
print(word[-2])
print(word[-5:])

# automated slicing
print(word.index("cali"))
print(word[word.index("cali"):word.index("fragi")])
print(word[word.index("docious"):])
print(word[word.index("fragilistic"):word.index("exp")] )