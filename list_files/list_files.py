import os
import time
import subprocess

def list_files(target_path, project_path):
    # Set up paths
    target_dir = target_path.split(os.path.sep)[-1]
    notes_path = os.path.join(target_path, "files.txt")

    list_target_dir(notes_path=notes_path, target_path=target_path, target_dir=target_dir)

    if project_path:
        os.chdir(project_path)
        list_git(notes_path=notes_path)

def list_target_dir(notes_path, target_path, target_dir):
    # Write list of files in target directory
    # Format for Markdown
    with open(notes_path, "w", encoding='utf-8') as f:
        f.writelines([f"**Files**: `{target_dir}`", "\n"])

        for path, subdirs, files in os.walk(target_path):
            if '.git' in subdirs:
                subdirs.remove('.git')
            for name in files:
                full_path = os.path.join(path, name)
                relative_path = full_path.split(target_dir, 1)[1]
                timestamp_str = time.strftime(  '%Y%m%d %H:%M:%S',
                                    time.gmtime(os.path.getmtime(full_path)))
                f.writelines(['\n', f'- `{relative_path}`  ', '\n', f'_Modified_: {timestamp_str} (UTC)' '\n', '  - Description: ', '\n'])

        f.writelines(['\n\n', '---'])

def list_git(notes_path):
    # os.chdir()
    # Get the project changes from Git
    subprocess.run('git', 'add', '-A')
    with subprocess.Popen(['git', 'diff', 'HEAD', '--name-status'], stdout=subprocess.PIPE) as proc:
        lines = proc.stdout.readlines()

    # Write the changes in a file, noting added, modified, etc.
    # Format for Markdown
        with open(notes_path, "a", encoding='utf-8') as f:
            f.write("\n\nGit changes:\n")
            for line in lines:
                text = line.decode('ascii').rstrip().split('\t')
                f.writelines(['\n- ', f"_{text[0]}_: `{text[1]}`", '\n  - Description:'])

if __name__ == "__main__":
    list_files(os.getcwd())