import pprint

def read_file(path1='1.txt', path2='2.txt', path3='3.txt'):
    result = []
    for path in [path1, path2, path3]:
        with open(path, 'r', encoding='utf-8') as f:
            file = f.readlines()
            result.append((path, len(file), file))
            result = sorted(result, key=lambda x: x[1])
    pprint.pprint(result)
    return result

def write_file():
    with open('4.txt', 'w', encoding='utf-8') as f:
        for name, num, text in read_file():
            f.write(f"{name}\n"
                    f"{num}\n"
            f"{''.join(text)}\n")

write_file()


