import subprocess
import sys
import os

def exitBuiltin() -> int:
    return (1)

def echoBuiltin(line: str) -> int:
    if line.count("'") % 2 == 0:
        line.replace("'", "")
    print(line)
    return (0)

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

def execProgram(line: str) -> int:
    if (checkOnPath(line, False)):
        subprocess.run(line.split())
        return (0)
    else:
        return (-1)

def pwdBuiltin() -> int:
    print(os.getcwd())
    return (0)

def cdBuiltin(line: str) -> int:
    if line.startswith("~"):
        line = line.replace("~", str(os.getenv("HOME")))
    elif not line.startswith("/"):
        line = os.getcwd() + "/" + line
    if os.path.exists(line):
        os.chdir(line)
    else:
        print("cd: " + line + ": No such file or directory")
    return (0)

def parse(line: str) -> int:
    if line == "exit":
        return (exitBuiltin())        
    if line.startswith("echo "):
        return (echoBuiltin(line[5:]))
    if line.startswith("type "):
        return (typeBuiltin(line[5:]))
    if line.startswith("pwd"):
        return (pwdBuiltin())
    if line.startswith("cd "):
        return (cdBuiltin(line[3:]))
    else:
        return(execProgram(line))

def main():
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

