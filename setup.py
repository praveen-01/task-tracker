from setuptools import setup

setup(
    name="task-tracker-cli",
    version="1.0",
    description="A task tracker CLI",
    py_modules=["task_tracker","task"],
    entry_points={
        "console_scripts": [
            "task-tracker-cli=task_tracker:main",
        ],
    },
    install_requires=[
        "tabulate",
    ],
    python_requires=">=3.6",
)