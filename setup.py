from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-ds11",
    version="0.1.1",
    author="NealWhitlock",
    author_email="datacreativellc@gmail.com",
    description="Example package for lambda school DS Unit 3",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/s2t2/lambdata-inclass-202002",
    keywords="lambda school",
    packages=find_packages() # ["my_lambdata"]
)