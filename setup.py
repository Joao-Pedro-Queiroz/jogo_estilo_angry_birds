from setuptools import setup, find_packages

setup(
    name="spatial_collapse",
    version="0.1.0",
    author="João Gabriel Faus Faraco, João Pedro Queiroz Viana",
    author_email="joaogff1@al.insper.edu, joaopqv@al.insper.edu.br",
    description="Uma recriação do Angry Birds Space em Pygame.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Joao-Pedro-Queiroz/spatial_collapse",
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
