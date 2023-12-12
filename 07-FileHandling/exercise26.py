import re
x ="To be, or not to be, that is the question"
pattern = r"[aeiouyAEIOUY]"
y = re.findall(pattern,x)
print(len(y))
