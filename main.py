import subprocess
import sys
import os

def exitBuiltin() -> int:
    return (1)

def echoBuiltin(line: str) -> int:
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
    elif line == "cd":
        print("cd is a shell builtin")
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
    if line.startswith("/"):
        os.chdir(line)
    return (0)

# def execLine(line: list) -> int:
#     pass

def parse(line: str) -> int:
    if line == "exit":
        return (exitBuiltin())        
    if line.startswith("echo "):
        return (echoBuiltin(line[5:]))
    if line.startswith("type "):
        return (typeBuiltin(line[5:]))
    if line.startswith("cd"):
        return (cdBuiltin(line[5:]))
    if line.startswith("pwd"):
        return (pwdBuiltin())
    else:
        return(execProgram(line))

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

# ## Building a Parser for a Bash Implementation
#
# A bash parser typically involves several stages. Here's the conceptual breakdown:
#
# **1. Lexical Analysis (Tokenizer/Lexer)**
#
# Before parsing, you need to break raw input into tokens. Bash tokens include words, operators (`|`, `&`, `;`, `<`, `>`), keywords (`if`, `for`, `while`), and quotes. Key challenges here are handling quoting rules (single, double, backslash), word splitting, and recognizing operators vs. word characters.
#
# **2. Grammar Definition**
#
# Bash has a formal grammar. Your parser needs to handle it in layers of precedence, roughly:
#
# - **Simple commands** — a word followed by arguments and redirections
# - **Pipelines** — commands connected with `|`
# - **Lists** — pipelines connected with `;`, `&`, `&&`, `||`
# - **Compound commands** — `if/then/fi`, `while/do/done`, `for`, `case`, subshells `()`, groups `{}`
# - **Function definitions**
#
# **3. Parsing Strategy**
#
# The most natural fit for bash is a **recursive descent parser** because the grammar is mostly context-free and hierarchical. You'd write one function per grammar rule (e.g., `parse_pipeline()`, `parse_list()`, `parse_command()`), each calling lower-level ones.
#
# **4. Building an AST (Abstract Syntax Tree)**
#
# As you parse, you construct tree nodes representing the structure — not just what the tokens are, but how they relate. For example, a pipe node has a left child and a right child. This is what the executor will later walk.
#
# **5. Key Bash-Specific Complexities**
#
# These are the tricky parts that make bash parsing harder than a typical language:
#
# - **Here-documents** (`<<`) require consuming lines after the current one
# - **Alias expansion** happens during parsing, not execution
# - **Command substitution** (`$(...)` or backticks) creates recursive parsing contexts
# - **Arithmetic expansion** (`$((...))`) has its own sub-grammar
# - **`[[` and `[`** have different parsing rules
# - **Context-sensitive keywords** — `do`, `done`, `fi` etc. are only keywords in certain positions
#
# **6. Error Recovery**
#
# A good parser should handle incomplete input gracefully (e.g., user typed `if foo` and hit enter — the shell should prompt for more with `>`), distinguish syntax errors from runtime errors, and provide meaningful messages.
#
# **Recommended Approach**
#
# 1. Start with the lexer — get tokenization solid first
# 2. Build a simple command parser, test it
# 3. Layer in pipelines, then lists
# 4. Add compound commands one at a time
# 5. Add the AST nodes alongside each parsing step
# 6. Leave here-docs and expansions for later
#
# Would you like to go deeper on any specific stage — the grammar rules, AST node design, or handling a particular construct like pipelines or compound commands?
