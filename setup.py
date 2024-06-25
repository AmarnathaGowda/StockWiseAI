from setuptools import find_packages,setup

setup(
    name = "StockWiseAI",
    version="0.0.1",
    author="Amarnath",
    author_email="amarnathagowda@gmail.com",
    packages=find_packages(),
    install_requires=["langchain","langchain-openai","langchain-astradb","datasets","pypdf","python-dotenv","flask"]
)