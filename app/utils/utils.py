import os

def checkOnPath(line: str, isTypeCommand: bool) -> int:
    paths = os.getenv("PATH", "").split(":")
    command = line.split()[0]
    for path in paths:
        fullPath = os.path.join(path, command)
        if os.path.isfile(fullPath):
            if os.access(fullPath, os.X_OK):
                if isTypeCommand:
                    print(command, "is", fullPath)
                return (1)
    return (0)

