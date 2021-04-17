s = """\
    $AAA
    $BBB
    $CCC
    $DDD
"""

# with open('test.txt', 'w+') as f:
#     f.write(s)
#     f.seek(0)
#     print(f.read())

# with open('test.txt', 'r') as f:
#     # print(f.read())
#     # while True:
#         # chunk = 2
#         # line = f.read(chunk)
#         # print(line)
#         # if not line:
#         #     break
#     print(f.tell())

import string

t = string.Template(s)
contents = t.substitute(AAA='まど', BBB='たん', CCC='しゅき', DDD='ぴ')
print(contents)