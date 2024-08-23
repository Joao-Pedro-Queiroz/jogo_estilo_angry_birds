from setuptools import setup, find_packages

setup(
    name="spatial_collapse",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,  # Isso permite que os dados especificados no MANIFEST.in sejam incluídos
    package_data={
     '': ['assets/img/*.png', 'spatial_collapse/assets/img/*.png',],  # Caminho relativo ao pacote
    },
    entry_points={
        'console_scripts': [
            'spatial_collapse=spatial_collapse.jogo:main',
        ],
    },
    author="João Gabriel Faus Faraco, João Pedro Queiroz Viana",
    author_email="joaogff1@al.insper.edu, joaopqv@al.insper.edu.br",
    description="Uma recriação do Angry Birds Space em Pygame.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Joao-Pedro-Queiroz/spatial_collapse",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)




# from setuptools import setup, find_packages

# setup(
#     name="spatial_collapse",
#     version="0.1.0",
#     packages=find_packages(),
#     install_requires = [
#     ],
#     package_data={
#         '': ['assets/img/*.png', 'spatial_collapse/assets/img/*.png',]
#     },
#   entry_points={
#         'console_scripts': [
#             'spatial_collapse=spatial_collapse.jogo:main',
#         ],
#     },
#     author="João Gabriel Faus Faraco, João Pedro Queiroz Viana",
#     author_email="joaogff1@al.insper.edu, joaopqv@al.insper.edu.br",
#     description="Uma recriação do Angry Birds Space em Pygame.",
#     long_description=open('README.md').read(),
#     long_description_content_type="text/markdown",
#     url="https://github.com/Joao-Pedro-Queiroz/spatial_collapse",
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
#     python_requires='>=3.6',
# )