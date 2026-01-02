import sys
import subprocess
import os

def run(cmd):
    subprocess.run(cmd, shell=True)

def clone_repo(url):
    run(f"git clone {url}")

def is_git_repo():
    return os.path.exists(".git")

def has_remote():
    result = subprocess.run(
        "git remote",
        shell=True,
        capture_output=True,
        text=True
    )
    return bool(result.stdout.strip())

def upload_project(repo_url=None):
    if not is_git_repo():
        print("📁 Initializing git repo")
        run("git init")

    run("git add .")
    run("git commit -m \"initial commit\"")

    if repo_url:
        print("🔗 Adding remote")
        run(f"git remote add origin {repo_url}")

    print("🚀 Pushing to GitHub")
    run("git branch -M main")
    run("git push -u origin main")

def main():
    if len(sys.argv) < 2:
        print("Usage: allicli [clone | upload]")
        return

    command = sys.argv[1]

    if command == "clone":
        clone_repo(sys.argv[2])

    elif command == "upload":
        repo_url = sys.argv[2] if len(sys.argv) > 2 else None
        upload_project(repo_url)

    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
