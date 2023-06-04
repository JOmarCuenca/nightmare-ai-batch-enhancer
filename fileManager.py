import os


class FileManager:

    __VALID_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}

    def __init__(self, outputPath):
        self.outputPath = outputPath

    def isDir(self):
        return os.path.isdir(self.outputPath)

    def isFile(self):
        return os.path.isfile(self.outputPath)

    def exists(self):
        return os.path.exists(self.outputPath)

    def getName(self):
        return os.path.splitext(self.outputPath)[0]

    def getExtension(path: str):
        return os.path.splitext(path)[1]

    def isValidExtension(path: str):
        extension = FileManager.getExtension(path)
        return extension in FileManager.__VALID_EXTENSIONS

    def getNextValidName(self, extension):
        counter = 1

        while True:
            path = ""
            if (self.isDir()):
                path = os.path.join(
                    self.getName(), f"output_img_{counter}{extension}")
            else:
                path = f"{self.getName()}_{counter}{extension}"

            if (not os.path.exists(path)):
                yield path
            else:
                counter += 1

    def getImagesDirs(self):
        assert self.isDir(), "Path is not a directory"
        return [os.path.join(self.outputPath, f) for f in os.listdir(self.outputPath) if FileManager.isValidExtension(f)]


if __name__ == '__main__':
    fm = FileManager("output.png")

    print(fm.exists())
    print(fm.isDir())
