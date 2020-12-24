s = """
AAA
BBB
CCC
FFF
"""
# with open('text.txt', 'w') as f:
#    f.write(s)

with open('text.txt', 'r') as f:
    while True:
        chunk = 2
        line = f.readline(chunk)
        print(line, end='')
        if not line:
            break
