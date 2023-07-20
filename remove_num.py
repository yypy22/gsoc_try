# from string import digits

# with open("wiki.txt") as f:
#     a = f.read()
#     translation_table = str.maketrans("", "", "0123456789")
#     a = a.translate(translation_table)
#     # a = a.replace(r'^[ 　]+', '')
#     for line in a:
#         a = a.lstrip()

# with open("wiki.txt", mode="w") as f:
#     f.write(a)
from string import digits

with open("wiki.txt") as f:
    a = f.read()
    translation_table = str.maketrans("", "", digits)
    a = a.translate(translation_table)
    # a = a.replace(r'^[ 　]+', '')  # This line is not needed

# Remove leading spaces from each line
lines = a.splitlines()
a = "\n".join(line.lstrip() for line in lines)

with open("wiki.txt", mode="w") as f:
    f.write(a)
