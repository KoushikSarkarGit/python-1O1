import os

YELLOW = "\033[38;2;255;215;0m"
BLACK = "\033[38;2;0;0;0m"
RED = "\033[38;2;255;0;0m"
RESET = "\033[0m"

if os.name == "nt":
    try:
        import ctypes

        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)
        if handle:
            mode = ctypes.c_ulong()
            if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
                kernel32.SetConsoleMode(handle, mode.value | 0x4)
    except Exception:
        pass

art = rf"""
{YELLOW}      /\_/\\
{YELLOW}     ( o.o )  {RED}●   ●{RESET}
{YELLOW}      > ^ <
{BLACK}    /  /  \\
{BLACK}   (__)  (__){RESET}
"""

print(art)
