from PIL import Image, ImageDraw
from modules.debug import Debug
from modules.crypt import pxcrypt

dbg = Debug("ERROR", "PXCERT-DRAWIMAGE")

class IMG:
    def saveimg(file_name: str | None = "undefinded", to_encode: str | None = lambda: dbg.err("Can't get variable 'RGBTable' (must be list)")) -> str:
        if to_encode == None:
            to_encode()
            return "Error raised. Abort"

        rgbtable: list = pxcrypt(to_encode).encodeToRGBTable()

        img_encoded = Image.new('RGB', (len(rgbtable) * 3, 3), 'black')
        pencil = ImageDraw.Draw(img_encoded)
        for i in range(len(rgbtable)):
            if i > 0:
                x = i * 3
                y = 0
                pencil.rectangle((x, y, x + 2, y + 2), fill=rgbtable[i])
            else:
                pencil.rectangle((0, 0, i + 2, 2), fill=rgbtable[i])

        img_encoded.save(f"{file_name[:20]}.png")
        return "Saved."

    def decodeimg(filePath: str | None = "") -> str:
        if filePath == "":
            dbg.err("Invalid file path")
            return ""
        print(filePath)

        try:
            imgToDecode = Image.open(filePath)
            imgToDecode_RGB = imgToDecode.convert("RGB")
            px = imgToDecode_RGB.load()
            pencil = ImageDraw.Draw(imgToDecode_RGB)
            width, height = imgToDecode_RGB.size
            rgbTable = []
            for i in range(int(width / 3)):
                if i > 0:
                    x = i * 3
                    rgbTable.append(px[x + 2, 1], )
                    pencil.rectangle((x + 1, 1, x + 1, 1), fill="black")

                else:
                    rgbTable.append(px[i + 1, 1], )
                    pencil.rectangle((i + 1, 1, i + 1, 1), fill="black")

            decodedText = pxcrypt.decodeFromRGBTables(rgbTable)
            file_name = decodedText.replace(" ", "_")
            imgToDecode_RGB.save(f"{file_name[:20]}_mask.png")
            return decodedText
        except FileNotFoundError:
            dbg.err("File not found.")
            return ""