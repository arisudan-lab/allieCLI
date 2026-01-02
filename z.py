import os

PROJECT_NAME = "allicli"

STRUCTURE = {
    PROJECT_NAME: {
        "allicli.py": """\
def main():
    print("allicli is running 🚀")

if __name__ == "__main__":
    main()
""",
        "git_utils.py": """\
# git related helpers
""",
        "config.py": """\
# config settings
""",
        "setup.py": """\
from setuptools import setup

setup(
    name="allicli",
    version="0.1",
    py_modules=["allicli"],
    entry_points={
        "console_scripts": [
            "allicli=allicli:main"
        ]
    }
)
""",
        "README.md": "# allicli\nA smart CLI tool\n"
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)

        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            if not os.path.exists(path):
                with open(path, "w") as f:
                    f.write(content)
                print(f"📄 Created {path}")
            else:
                print(f"⚠️ Skipped {path} (already exists)")

create_structure(".", STRUCTURE)
print("✅ Project structure created")
