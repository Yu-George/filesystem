class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.subdirectories = {}
        self.files = []
        self.parent = parent

class FileSystem:
    def __init__(self):
        self.root = Directory("/", None)
        self.fullpath = "/"
    def cd(self, path):
        if path == "..":
            # Check if current directory is root
            if self.current_dir.name != "/":
                self.current_dir = self.current_dir.parent
        else:
            if path in self.current_dir.subdirectories:
                self.current_dir = self.current_dir.subdirectories[path]
            else:
                print("Directory does not exist")

    def ls(self):
        print("Directories:")
        for directory in self.current_dir.subdirectories:
            print(directory)
        print("Files:")
        for file in self.current_dir.files:
            print(file)

    def mkdir(self, directory_name):
        new_directory = Directory(directory_name, self.current_dir, self.current_dir.path)
        self.current_dir.subdirectories[directory_name] = new_directory

    def touch(self, file_name):
        self.current_dir.files.append(file_name)

    def main(self):
        self.current_dir = self.root
        while True:
            command = input(f"{self.current_dir.name}$ ")
            if command == "exit":
                break
            elif command.split()[0] == "cd":
                self.cd(command.split()[1])
            elif command == "ls":
                self.ls()
            elif command.split()[0] == "mkdir":
                self.mkdir(command.split()[1])
            elif command.split()[0] == "touch":
                self.touch(command.split()[1])
            else:
                print("Invalid command")


if __name__ == "__main__":
    fs = FileSystem()
    fs.main()