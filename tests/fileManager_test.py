import unittest
from fileManager import FileManager

class TestFileManager(unittest.TestCase):

    def test_isDir(self):
        fm = FileManager("output.png")
        self.assertFalse(fm.isDir())

        fm = FileManager("tests")
        self.assertTrue(fm.isDir())

    def test_isFile(self):
        fm = FileManager("main.py")
        self.assertTrue(fm.isFile())

        fm = FileManager("tests")
        self.assertFalse(fm.isFile())

    def test_extension_getter(self):
        self.assertEqual(FileManager.getExtension("output.png"), ".png")
        self.assertEqual(FileManager.getExtension("output.jpg"), ".jpg")
        self.assertEqual(FileManager.getExtension("output.jpeg"), ".jpeg")
        self.assertEqual(FileManager.getExtension("output.webp"), ".webp")

    def test_extension_valid(self):
        self.assertTrue(FileManager.isValidExtension("output.png"))
        self.assertTrue(FileManager.isValidExtension("output.jpg"))
        self.assertTrue(FileManager.isValidExtension("output.jpeg"))
        self.assertTrue(FileManager.isValidExtension("output.webp"))
        self.assertFalse(FileManager.isValidExtension("output.txt"))
        self.assertFalse(FileManager.isValidExtension("output.pdf"))
        self.assertFalse(FileManager.isValidExtension("output.docx"))
        self.assertFalse(FileManager.isValidExtension("output.py"))

    def test_get_name(self):
        fm = FileManager("main.py")
        self.assertEqual(fm.getName(), "main")

        fm = FileManager("tests")
        self.assertEqual(fm.getName(), "tests")

    def test_next_valid_name(self):
        fm = FileManager("main.py")
        extension = FileManager.getExtension("main.py")
        nextName = fm.getNextValidName(extension)
        self.assertEqual(next(nextName), "main_1.py")