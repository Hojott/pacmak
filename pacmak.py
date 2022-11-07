import sys, subprocess

printmode = False
for i in sys.argv[1]:
    if i == "p":
        printmode = True
    elif i == "S":
        syncmode = True

if printmode:
    stdout = subprocess.run(["pacman"]+sys.argv[1:], capture_output=True).stdout
    print(stdout)

elif syncmode:
    subprocess.run(["pacman"]+sys.argv[1:]+["--print", "--print-format", "%n", "--noprogressbar"], check=True, capture_output=True).stdout
    packages = stdout.split()

