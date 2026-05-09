import sys
import os

def exitBuiltin() -> int:
    return (1)

def echoBuiltin(line: str) -> int:
    print(line)
    return (0)

def checkOnPath(line: str) -> int:
    paths = os.getenv("PATH", "").split(":")
    for path in paths:
        fullPath = os.path.join(path, line)
        if os.path.isfile(fullPath):
            if os.access(fullPath, os.X_OK):
                print(line, "is", fullPath)
                return (1)
    return (0)

def typeBuiltin(line: str) -> int:
    if line == "type":
        print("type is a shell builtin")
    elif line == "echo":
        print("echo is a shell builtin")
    elif line == "exit":
        print("exit is a shell builtin")
    else :
        if (checkOnPath(line) == 0):
            print(line + ": not found")
    return (0)

def parse(line: str) -> int:
    if line == "exit":
        return (exitBuiltin())        
    if line.startswith("echo "):
        return (echoBuiltin(line[5:]))
    if line.startswith("type"):
        return (typeBuiltin(line[5:]))
    return (-1)

def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        line = input()
        returnStatus = parse(line)
        if returnStatus == 1:
            return
        elif returnStatus == -1:
            print(line + ": command not found")

if __name__ == "__main__":
    main()

