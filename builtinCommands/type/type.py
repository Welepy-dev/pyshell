from utils.utils import checkOnPath

def typeBuiltin(line: str) -> int:
    if line == "type":
        print("type is a shell builtin")
    elif line == "echo":
        print("echo is a shell builtin")
    elif line == "exit":
        print("exit is a shell builtin")
    elif line == "pwd":
        print("pwd is a shell builtin")
    else :
        if (checkOnPath(line, True) == 0):
            print(line + ": not found")
            return (0)
    return (0)

