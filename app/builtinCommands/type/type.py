from app.utils.utils import checkOnPath

def typeBuiltin(args: list) -> int:
    if len(args) != 1:
        print("Type needs one argument and one argument only")
        return (1)
    if args[0] == "type":
        print("type is a shell builtin")
    elif args[0] == "echo":
        print("echo is a shell builtin")
    elif args[0] == "exit":
        print("exit is a shell builtin")
    elif args[0] == "pwd":
        print("pwd is a shell builtin")
    else:
        if (checkOnPath(args[0], True) == 0):
            print(args[0] + ": not found")
            return (0)
    return (0)

