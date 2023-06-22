from PIL import Image, ImageDraw

from modules.drawimg import IMG
if __name__ == "__main__":
    print("                            ")
    print("1. Encode text to PNG       ")
    print("2. Decode PNG               ")
    print("                            ")
    choise = input("Selector: ")
    match str(choise):
        case "1":
            to_encode = input("Enter text to encode: ")
            file_name = input("File name: ")

            print(IMG.saveimg(file_name=file_name.replace(".", ""), to_encode=to_encode))

        case "2":
            filePath = input("Path to file: ")
            print(IMG.decodeimg(filePath))
        case _:
            print("\nInvalid choise. Restart app")