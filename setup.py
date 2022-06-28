import setuptools

setuptools.setup(
    name="ypass",
    version="0.1.0",
    author="Georgios Atheridis",
    author_email="atheridis@tutamail.com",
    description="Simple Password Manager",
    url="https://github.com/atheridis/ypass-temp.git",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "ypass=ypass.main:main",
        ],
    },
    install_requires=[
        "pyperclip",
    ],
    python_requires=">=3.7",
)
