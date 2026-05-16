def echoBuiltin(line: str) -> int:
    if line.count("'") % 2 == 0:
        line.replace("'", "")
    print(line)
    return (0)


