import subprocess

# Get the changes from Git
with subprocess.Popen(["git", "diff", "HEAD", "--name-status"], stdout=subprocess.PIPE) as proc:
    lines = proc.stdout.readlines()

# Write the changes in a file, noting added, modified, etc.
    with open("git-files.md", "a", encoding="utf-8") as f:
        f.write("\n\nGit changes:")
        for line in lines:
            text = line.decode('ascii').rstrip().split('\t')
            f.writelines(['\n- ', f"_{text[0]}_: `{text[1]}`", '\n  -'])