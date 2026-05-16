from builtinCommands.cd.cd import cdBuiltin
from builtinCommands.pwd.pwd import pwdBuiltin
from builtinCommands.echo.echo import echoBuiltin
from builtinCommands.exit.exit import exitBuiltin
from builtinCommands.type.type import typeBuiltin
from builtinCommands.clear.clear import clearBuiltin
from utils.utils import checkOnPath

import subprocess
import sys

def execProgram(line: str) -> int:
    if (checkOnPath(line, False)):
        subprocess.run(line.split())
        return (0)
    else:
        return (-1)

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
    if line.startswith("clear"):
        return (clearBuiltin())
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
