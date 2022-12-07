class FS_Node:
    def __init__(self, name, parent = None, size = 0):
        self.name = name
        self.size = size # Size of file (0 if directory)
        self.children = {}
        self.parent = parent

    def is_dir(self) -> bool:
        return self.size == 0

    def cd(self, dir_name) -> "FS_Node":
        if dir_name == "..": # Go up a directory
            return self.parent
        else: # Go down a directory
            return self.children[dir_name]

    def touch(self, file_name, size = 0) -> "FS_Node":
        # Check if file already exists
        if file_name in self.children:
            return self.children[file_name]
        else:
            # Create a new FS_Node object for the file
            self.children[file_name] = FS_Node(file_name, self, size)
            return self.children[file_name]

    def get_size(self) -> int:
        # If it's a file, return its size
        if self.is_dir():
            # If it's a directory, return the sum of its children's sizes
            total_size = 0
            for child in self.children.values():
                total_size += child.get_size()
            return total_size
        else:
            return self.size

    def get_all_dirs(self):
        if self.is_dir():
            yield self
        for child in self.children.values():
            yield from child.get_all_dirs()

    # repr() method (for debugging view)
    def __repr__(self) -> str:
        return self.__str__()

    # str() method
    def __str__(self) -> str:
        fs_node_type = "dir" if self.is_dir() else "file"
        return f"{fs_node_type}, name: {self.name}, size: {self.size}, children: {self.children}"
