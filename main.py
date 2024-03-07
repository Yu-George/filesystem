class Directory:
    def __init__(self, name, parent, path):
        self.name = name
        self.subdirectories = {}
        self.files = []
        self.parent = parent
        self.path = path

class FileSystem:
    def __init__(self):
        self.root = Directory("/", None, "/")
