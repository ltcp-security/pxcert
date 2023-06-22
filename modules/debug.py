import colorama


#
# Available logger levels
# INFO - Info called by Debug.info
# ERROR - Info called by Debug.err and Debug.info
# DEBUG - Info called by Debug.err and Debug.info and Debug.dbg
#

class Debug:
    def __init__(self, lvl: str | None = "INFO", prefix: str | None = "APPNAME"):
        self.prefix = prefix
        self.lvl = lvl

    def dbg(self, *msgs, sep: str | None = " ") -> None:
        toprint = f"[{self.prefix}] :: [{colorama.Fore.LIGHTYELLOW_EX}DEBUG{colorama.Fore.RESET}] "
        if self.lvl != "DEBUG":
            return

        for a in range(len(msgs)):
            if a != len(msgs) - 1:
                toprint += str(msgs[a]) + sep
            else:
                toprint += str(msgs[a])

        print(toprint.replace("\n", ""))

    def info(self, *msgs, sep: str | None = " ") -> None:
        toprint = f"[{self.prefix}] :: [{colorama.Fore.LIGHTGREEN_EX}INFO{colorama.Fore.RESET}] "
        if self.lvl != "ERROR":
            if self.lvl != "DEBUG":
                if self.lvl != "INFO":
                    return

        for a in range(len(msgs)):
            if a != len(msgs) - 1:
                toprint += str(msgs[a]) + sep
            else:
                toprint += str(msgs[a])

        print(toprint.replace("\n", ""))

    def err(self, *msgs, sep: str | None = " ") -> None:
        toprint = f"[{self.prefix}] :: [{colorama.Fore.RED}ERROR{colorama.Fore.RESET}] "
        if self.lvl != "ERROR":
            if self.lvl != "DEBUG":
                return

        for a in range(len(msgs)):
            if a != len(msgs) - 1:
                toprint += str(msgs[a]) + sep
            else:
                toprint += str(msgs[a])

        print(toprint.replace("\n", ""))