x = "To be, or not to be, that is the question"
import re
pattern = r"\b\w+\b"
y = re.findall(pattern,x)
print(len(y))