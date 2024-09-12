from setuptools import find_packages,setup

setup(
    
    name="MCQ Generator using Generative AI",
    author="Parthiv Shah",
    version="0.0.1",
    author_email="parthivshah33@gmail.com",
    packages=find_packages(),
    install_requires = ['openai','langchain','python-dotenv','streamlit','PyPDF2']
    
    
)