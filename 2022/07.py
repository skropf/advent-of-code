class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.folders = []
        self.files = {}
        self.size = 0
    
    def __repr__(self):
        return self.name + ": size: " + str(self.size) + ", folders: " + str(len(self.folders)) + ", files: " + str(len(self.files))

    def calc_size(self):
        def walk_folders(folder):
            for f in folder.folders:
                yield from walk_folders(f)

            for filesize in folder.files.values():
                yield filesize

        sizes = walk_folders(self)
        self.size = sum([s for s in sizes])
    
def _get_root(folder):
    if folder.parent == None: return folder

    return _get_root(folder.parent)

def _process_command(cmd, folder):
    command = cmd[0].split(' ')[1]

    if command == "cd":
        path = cmd[0].split(' ')[2]
        if path == "/":
            return _get_root(folder)
        elif path == "..":
            return folder.parent
        else:
            new_folder = Folder(path, folder)
            folder.folders.append(new_folder)
            return new_folder

    if command == "ls":
        for line in cmd[1:]:
            elems = line.split(' ')

            if elems[0] != "dir": folder.files[elems[1]] = int(elems[0])

def _calc_folder_sizes(folder):
    folder.calc_size()
    for f in folder.folders:
        _calc_folder_sizes(f)

def populate_filesystem(cmds, folder):
    cmd = []

    for line in cmds:
        if line.startswith('$'):
            if cmd:
                new_folder = _process_command(cmd, folder)
                if new_folder: folder = new_folder
                cmd = [line.strip()]
            else:
                cmd.append(line.strip())
        else: cmd.append(line.strip())

    _calc_folder_sizes(_get_root(folder))

def get_folders_below_100000(folder):
    for f in folder.folders:
        yield from get_folders_below_100000(f)

    if folder.size < 100000: yield folder
    
def get_folder_to_delete(folder, needed_space):
    for f in folder.folders:
        yield from get_folder_to_delete(f, needed_space)
    
    if folder.size >= needed_space: yield folder


cmds = open('07.input', 'r').readlines()
root = Folder("/", None)

populate_filesystem(cmds, root)

print(sum([x.size for x in get_folders_below_100000(root)]))

max_space = 70000000
update_space = 30000000
free_space = max_space - root.size

print(min([x.size for x in get_folder_to_delete(root, update_space - free_space)]))