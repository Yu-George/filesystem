import unittest
from main import FileSystem


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()
        self.fs.current_dir = self.fs.root

    def test_mkdir_single(self):
        self.fs.mkdir(["testDir"])
        self.assertTrue("testDir" in self.fs.current_dir.subdirectories)

    def test_mkdir_2_dir_deep(self):
        self.fs.mkdir(["testDir1/testDir2"])
        self.assertTrue("testDir1" in self.fs.current_dir.subdirectories)
        self.assertTrue("testDir2" in self.fs.current_dir.subdirectories["testDir1"].subdirectories)

    def test_mkdir_multiple(self):
        self.fs.mkdir(["testDir1", "testDir2"])
        self.assertTrue(
            "testDir1" in self.fs.current_dir.subdirectories and "testDir2" in self.fs.current_dir.subdirectories)

    def test_mkdir_invalid(self):
        self.fs.mkdir("invalid?")
        self.assertFalse("invalid?" in self.fs.current_dir.subdirectories)

    def test_cd(self):
        self.fs.mkdir(["dir1"])
        self.fs.cd("dir1")
        self.assertEqual(self.fs.current_dir.name, "dir1")

    def test_cd_2_dir_deep(self):
        self.fs.mkdir(["dir1/dir2"])
        self.fs.cd("dir1/dir2")
        self.assertEqual(self.fs.current_dir.name, "dir2")

    def test_cd_home(self):
        self.fs.mkdir(["dir1"])
        self.fs.cd("dir1")
        self.fs.cd("")
        self.assertEqual(self.fs.current_dir.name, "")

    def test_touch(self):
        self.fs.touch("file.txt")
        self.assertTrue("file.txt" in self.fs.current_dir.files)

    def test_touch_invalid(self):
        self.fs.touch("invalid?")
        self.assertFalse("invalid?" in self.fs.current_dir.files)


if __name__ == '__main__':
    unittest.main()
