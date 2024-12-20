import re
import typing
import dataclasses


print("Day03")
with open('day03/input.txt') as f:
    txt = f.read()


State = dict[str,typing.Any]
ArgTuple = tuple[typing.Any,...]
Instr = typing.Callable[[State, ArgTuple], typing.NoReturn]
@dataclasses.dataclass
class Command:
    keyword: str
    arg_pattern: str
    func: Instr

def Process(txt: str, state: State, commands: dict[str, Command]):
    pats = "|".join(f"{k}{v.arg_pattern}" for k,v in commands.items())
    for m in re.finditer(re.compile(pats, re.MULTILINE), txt):
        command = m.group(0).split("(")[0]
        if command in commands:
            commands[command].func(state, m.groups())
    print(state)
    return state


# Part One
def mul(state: State, args: ArgTuple):
    state["total"] = state.get("total", 0) + int(args[0]) * int(args[1])
mul_cmd = Command("mul", r"\((\d{1,3}),(\d{1,3})\)", mul)
commands = {
    "mul": mul_cmd
}
state = {}
Process(txt, state, commands)


#Part Two
class enable_wrapper:
    def __init__(self, wrapped_cmd: Instr):
        self.instr = wrapped_cmd
    def __call__(self, state, args):
        if state.get("enabled", True):
            return self.instr(state, args)
        return None
def enable(state: State, _: ArgTuple):
    state["enabled"] = True
def disable(state, _: ArgTuple):
    state["enabled"] = False
commands = {
    "mul":   Command(mul_cmd.keyword, mul_cmd.arg_pattern, enable_wrapper(mul)),
    "don't": Command("don't", r"\(\)", disable),
    "do":    Command("do",    r"\(\)", enable),
}
state = {}
Process(txt, state, commands)