from setuptools import setup,find_packages

setup(
    name="pypi-package-demo",
    version="0.0.1",
    author="Deepak Mishra",
    author_email="deepak.mishra2@gmail.com",
    description="A demo pip package for Gitlab pacakge resistry",
    package=find_packages(),
    classifiers=["Python 3.9", "Gitlab Demo", "Cross Platfomr"],
    python_requires='>=3.5'
)
