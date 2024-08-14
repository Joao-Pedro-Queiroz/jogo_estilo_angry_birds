from setuptools import setup, find_packages

setup(
    name="jogo_estilo_angry_birds",
    version="0.1.0",
    author="Joao Gabriel Faraco, Joao Pedro",
    author_email="joaogff1@al.insper.edu",
    description="Uma recriação do Angry Birds Space em Pygame.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Joao-Pedro-Queiroz/jogo_estilo_angry_birds",
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

# setup(
#     name="jogo_estilo_angry_birds",              # Nome do pacote
#     version="0.1.0",              # Versão do pacote
#     packages=find_packages(),     # Inclui todos os pacotes Python no diretório

#     # Informações adicionais
#     description="Um jogo simples usando Pygame",
#     long_description=open('README.md').read(),  # Leia o conteúdo do README
#     long_description_content_type='text/markdown',

#     # Dependências do projeto
#     install_requires=[
#         "pygame>=2.0.0",
#     ],

#     # Metadados adicionais
#     author="Joao Gabriel e Joao Pedro",
#     author_email="joaogff1@al.insper.com",
#     url="https://github.com/Joao-Pedro-Queiroz/jogo_estilo_angry_birds",
    
#     # Classificações (opcional)
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#         "Topic :: Games/Entertainment",
#     ],
    
#     # Entry points (opcional, se você quiser um script executável)
#     entry_points={
#         'console_scripts': [
#             'jogo_estilo_angry_birds=jogo_estilo_angry_birds.jogo:main',  # Substitua por sua função principal
#         ],
#     },
    
#     python_requires='>=3.6',
# )
