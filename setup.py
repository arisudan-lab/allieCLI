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
