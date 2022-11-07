import sys, subprocess#, os

printmode = False
syncmode = False
artixmode = False

#os.getenv()

for i in sys.argv[1]:
    if i == "S":
        syncmode = True
    if i == "p":
        printmode = True

if printmode:
    pacman_command = ["pacman"]+sys.argv[1:]
    print(subprocess.run(pacman_command, capture_output=True).stdout)

elif syncmode:
    getpackages_command = ["pacman"] + sys.argv[1:] + ["--print", "--print-format", "%n", "--noprogressbar", "--noconfirm"]
    stdout = subprocess.run(getpackages_command, capture_output=True).stdout
    packages = stdout.split()
    
    if artixmode:
        for pack in packages:
            git_command = ["git", "clone", "https://github.com/artixlinux/main/"+pack+".git"]
            print(subprocess.run(git_command, capture_output=True).stdout)
    else:
        asp_command = ["asp", "export"] + packages
        print(subprocess.run(asp_command, capture_output=True).stdout)
    
    for pack in packages:
        make_command = ["cd", pack, "&&", "makepkg", "-sci"]
        print(subprocess.run(make_command, capture_output=True).stdout)

else:
    pacman_command = ["pacman"]+sys.argv[1:]
    print(subprocess.run(pacman_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout)