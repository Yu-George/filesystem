import re


class Directory:
    def __init__(self, name, parent, path):
        self.name = name
        self.subdirectories = {}
        self.files = []
        self.parent = parent
        self.path = path


class FileSystem:
    def __init__(self):
        self.current_dir = None
        self.root = Directory("", None, "")

    def cd(self, path):
        # go back 1 level
        if path == "..":
            # check if root
            if self.current_dir.name != "":
                self.current_dir = self.current_dir.parent
        # go back to root
        elif path == "~" or path == "":
            self.current_dir = self.root
        else:
            directories = path.split("/")
            for d in directories:
                print(d)
                if d == "":
                    continue
                if d in self.current_dir.subdirectories:
                    self.current_dir = self.current_dir.subdirectories[d]
                else:
                    print("Directory does not exist")
                    break

    def ls(self):
        print("Directories:")
        for directory in self.current_dir.subdirectories:
            print("\t-" + directory)
        print("Files:")
        for file in self.current_dir.files:
            print("\t-" + file)

    def mkdir(self, paths):
        for path in paths:
            directories = path.split("/")
            current_dir = self.current_dir
            for d in directories:
                if d not in current_dir.subdirectories:
                    if not re.match('^[^<>:"/\\|?*]+$', d):
                        print("Invalid directory name")
                    else:
                        new_directory = Directory(d, current_dir, current_dir.path + "/" + d)
                        current_dir.subdirectories[d] = new_directory
                current_dir = current_dir.subdirectories[d]

    def touch(self, file_name):
        if not re.match('^[^<>:"/\\|?*]+$', file_name):
            print("Invalid file name")
        else:
            self.current_dir.files.append(file_name)

    def main(self):
        self.current_dir = self.root
        while True:
            command = input(f"{self.current_dir.path}$ ")
            match command.split():
                case ["exit"]:
                    break
                case ["cd", path]:
                    self.cd(path)
                case ["mkdir", *dirs]:
                    self.mkdir(dirs)
                case ["ls"]:
                    self.ls()
                case ["touch", file]:
                    self.touch(file)
                case _:
                    print("Invalid Command")

if __name__ == "__main__":
    fs = FileSystem()
    fs.main()
