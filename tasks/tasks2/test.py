def folder_name(names: list):
    names.sort(key=len)
    longest_name = names.pop()
    length = len(longest_name)
    needed = length - len(set(longest_name))
    while True:
        name = names.pop()
        if len(set(name)) == len(name):
            out = name
            break
    out += "_" * needed
    return out
