import time
import random
import subprocess
from datetime import datetime

REPO_PATH = r"C:\path\to\your\git\repo"   # change this
COMMITS_PER_DAY = 12

def make_commit():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("fakecommit.txt", "a") as f:
        f.write(f"Commit at {now}\n")

    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"auto commit {now}"])
    subprocess.run(["git", "push", "origin", "main"])

    print(f"✅ Commit done at {now}")

while True:
    commits_today = random.randint(COMMITS_PER_DAY - 2, COMMITS_PER_DAY + 2)

    for _ in range(commits_today):
        make_commit()

        # wait random time between commits (30–120 minutes)
        sleep_time = random.randint(1800, 7200)
        time.sleep(sleep_time)

    # sleep till next day
    print("🌙 Sleeping till next day...")
    time.sleep(24 * 60 * 60)

