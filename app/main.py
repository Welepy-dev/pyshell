from .builtinCommands.cd.cd import cdBuiltin
from .builtinCommands.pwd.pwd import pwdBuiltin
from .builtinCommands.echo.echo import echoBuiltin
from .builtinCommands.exit.exit import exitBuiltin
from .builtinCommands.type.type import typeBuiltin
from .builtinCommands.clear.clear import clearBuiltin

import sys
import shlex
import shutil
import subprocess

def execProgram(cmd: str, args: list) -> int:
    path = shutil.which(cmd)
    if path:
        subprocess.run([cmd] + args, executable=path)
        return (0)
    else:
        return (-1)

def parse(cmd: str, args: list) -> int:
    if cmd == "exit":
        return (exitBuiltin())        
    if cmd == "echo":
        return (echoBuiltin(args))
    if cmd == "type":
        return (typeBuiltin(args))
    if cmd == "pwd":
        return (pwdBuiltin())
    if cmd == "cd":
        return (cdBuiltin(args))
    if cmd == "clear":
        return (clearBuiltin())
    else:
        return(execProgram(cmd, args))

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        line = input().strip()

        if not line:
            continue

        parts = shlex.split(line)
        cmd = parts[0]

        returnStatus = parse(cmd, parts[1:])
        if returnStatus == 1:
            return
        elif returnStatus == -1:
            print(cmd + ": command not found")

if __name__ == "__main__":
    main()
