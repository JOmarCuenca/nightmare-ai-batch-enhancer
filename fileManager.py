import os


class FileManager:

    __VALID_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
    counter = 1

    def __init__(self, path):
        self.path = path

    def isDir(self):
        return os.path.isdir(self.path)

    def isFile(self):
        return os.path.isfile(self.path)

    def exists(self):
        return os.path.exists(self.path)

    def getName(self):
        return os.path.splitext(self.path)[0]

    def getExtension(path: str):
        return os.path.splitext(path)[1]

    def isValidExtension(path: str):
        extension = FileManager.getExtension(path)
        return extension in FileManager.__VALID_EXTENSIONS

    def getNextValidName(self, extension):
        

        while True:
            path = ""
            if (self.isDir()):
                path = os.path.join(
                    self.getName(), f"output_img_{self.counter}{extension}")
            else:
                path = f"{self.getName()}_{self.counter}{extension}"

            if (not os.path.exists(path)):
                return path
            else:
                self.counter += 1

    def getImagesDirs(self):
        assert self.isDir(), "Path is not a directory"
        return [os.path.join(self.path, f) for f in os.listdir(self.path) if FileManager.isValidExtension(f)]


if __name__ == '__main__':
    fm = FileManager("output.png")

    print(fm.exists())
    print(fm.isDir())
