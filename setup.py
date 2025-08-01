from setuptools import setup, find_packages

setup(
    name="sarif-to-gitlab-sast",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "sarif-to-gitlab=cli:main"
        ]
    },
)
