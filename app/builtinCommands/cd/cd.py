import os

def cdBuiltin(args: list) -> int:
    homepath = str(os.getenv("HOME"))
    if len(args) == 0:
        os.chdir(homepath)
        return (0)
    if len(args) > 1:
        print("Too many arguments")
        return (1)
    if args[0].startswith("~"):
        args[0] = args[0].replace("~", str(os.getenv("HOME")))
    elif not args[0].startswith("/"):
        args[0] = os.getcwd() + "/" + args[0]
    if os.path.exists(args[0]):
        os.chdir(args[0])
    else:
        print("cd: " + args[0] + ": No such file or directory")
    return (0)
