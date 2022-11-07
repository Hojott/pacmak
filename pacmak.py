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
    print(subprocess.run(pacman_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout)

elif syncmode:
    getpackages_command = ["sudo","pacman"] + sys.argv[1:] + ["--print", "--print-format", "%n", "--noprogressbar", "--noconfirm"]
    stdout = subprocess.run(getpackages_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout
    packages = stdout.split()
    
    if artixmode:
        for pack in packages:
            git_command = ["mkdir", pack, "&&", "cd", pack, "&&", "wget", "https://raw.githubusercontent.com/artix-linux/main/master/"+pack+"/trunk/PKGBUILD", "&&", "cd", ".."]
            git_clone = subprocess.run(git_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout
            print(git_clone)
            if git_clone.returncode == 128:
                asp_command = ["asp", "export", pack]
                print(subprocess.run(asp_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout)
    else:
        asp_command = ["asp", "export"] + packages
        print(subprocess.run(asp_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout)
    
    for pack in packages:
        make_command = ["cd", pack, "&&", "makepkg", "-sci"]
        print(subprocess.run(make_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout)

else:
    pacman_command = ["pacman"]+sys.argv[1:]
    print(subprocess.run(pacman_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout)