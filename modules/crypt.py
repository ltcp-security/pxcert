from modules.debug import Debug

dbg = Debug("ERROR", "PXCERT-CRYPT")


class pxcrypt():
    def __init__(self, text: str | None = None):
        if text != None:
            self.text = text.lower()

    __alphabet = {
        33: '!',
        64: '@',
        35: '#',
        36: '$',
        38: '&',
        95: '_',
        43: '+',
        34: '"',
        59: ';',
        37: '%',
        58: ':',
        63: '?',
        42: '*',
        40: '(',
        41: ')',
        45: '-',
        61: '=',
        126: '~',
        47: '/',
        92: '\\',
        46: '.',
        44: ',',
        91: '[',
        93: ']',
        94: "^",
        123: '{',
        125: '}',
        60: '<',
        62: '>',
        32: ' ',
        39: "'",
        49: '1',
        50: '2',
        51: '3',
        52: '4',
        53: '5',
        54: '6',
        55: '7',
        56: '8',
        57: '9',
        48: '0',
        97: 'a',
        98: 'b',
        99: 'c',
        100: 'd',
        101: 'e',
        102: 'f',
        103: 'g',
        104: 'h',
        105: 'i',
        106: 'j',
        107: 'k',
        108: 'l',
        109: 'm',
        110: 'n',
        111: 'o',
        112: 'p',
        113: 'q',
        114: 'r',
        115: 's',
        116: 't',
        117: 'u',
        118: 'v',
        119: 'w',
        120: 'x',
        121: 'y',
        122: 'z',
        124: '|',
        171: 'а',
        170: 'б',
        169: 'в',
        168: 'г',
        167: 'д',
        166: 'е',
        201: 'ё',
        165: 'ж',
        164: 'з',
        163: 'и',
        162: 'й',
        161: 'к',
        160: 'л',
        159: 'м',
        158: 'н',
        157: 'о',
        156: 'п',
        218: 'р',
        217: 'с',
        216: 'т',
        215: 'у',
        214: 'ф',
        213: 'х',
        212: 'ц',
        211: 'ч',
        210: 'ш',
        209: 'щ',
        208: 'ъ',
        207: 'ы',
        206: 'ь',
        205: 'э',
        204: 'ю',
        203: 'я',
    }

    def encodeToRGBTable(self):
        dbg.info("encoding text...")
        hashstr = []
        for c in range(0, len(self.text)):
            if int(hex(ord(self.text[c])), 16) < 1000:
                hashstr.append(int(str(hex(ord(self.text[c]))), 16))
            else:
                hashstr.append((300 - (int.from_bytes(self.text[c].encode(), byteorder="little")) % 255))

        charshex = []
        for c in range(0, len(self.text)):
            charshex.append(hex(ord(self.text[c])), )

        hashnum = []
        for b in range(0, len(hashstr)):
            hashnum.append(hashstr[b])

        for a in range(0, len(hashnum)):
            dbg.dbg(self.text[a], charshex[a], hashstr[a], sep="  -  ")

        dbg.info("size of symbols:", len(hashnum))
        rgbTables = []
        while len(hashnum) >= 3:
            pseudoTable = ()
            for i in range(3):
                pseudoTable += (hashnum[i],)

            for i in range(len(pseudoTable)):
                hashnum.remove(pseudoTable[i])

            rgbTables += [pseudoTable, ]

            pseudoTable = ()

        dbg.dbg("tables:", rgbTables)
        dbg.dbg("symbnums:", hashnum)
        pseudoTable = ()
        if len(hashnum) < 3 and len(hashnum) > 0:
            for i in range(len(hashnum)):
                pseudoTable += (hashnum[i],)

            for i in range(len(pseudoTable)):
                hashnum.remove(hashnum[0])

            while len(pseudoTable) < 3:
                pseudoTable += (0,)

            rgbTables += [pseudoTable, ]
            dbg.dbg("pseudo table:", pseudoTable)
            pseudoTable = ()
            dbg.dbg("cleared symbnums:", hashnum)

        dbg.dbg("done table:", rgbTables)
        dbg.info("size of table:", len(rgbTables))
        dbg.info("hex colors:", pxcrypt.rgb2hex(rgbTables))

        return rgbTables

    def decodeFromRGBTables(rgbTables: list):
        dbg.info("decoding table...")
        dbg.info("size of table", len(rgbTables))
        dbg.dbg("elements ~")
        for a in range(len(rgbTables)):
            dbg.dbg(f"{a + 1}.", rgbTables[a])

        allNums = ()
        for a in range(len(rgbTables)):
            for b in range(len(rgbTables[a])):
                allNums += (rgbTables[a][b],)
        allNums = list(filter(lambda num: num != 0, list(allNums)))

        dbg.info("all numbers:", allNums)
        dbg.info("size of encoded symbols:", len(allNums))

        decodedMsg = ""
        for a in range(len(allNums)):
            decodedMsg += pxcrypt.__alphabet.get(allNums[a])

        return decodedMsg

    def rgb2hex(rgbTables):
        doneStr = ""
        for i in range(len(rgbTables)):
            doneStr += "#{:02x}{:02x}{:02x}".format(rgbTables[i][0], rgbTables[i][1], rgbTables[i][2]) + " "

        return doneStr