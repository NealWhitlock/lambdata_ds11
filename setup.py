from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-NealWhitlock",
    version="0.1.3",
    author="NealWhitlock",
    author_email="nealwhitlock@gmail.com",
    description="Example package for lambda school DS Unit 3",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/NealWhitlock/lambdata_ds11",
    keywords="lambda school",
    packages=find_packages() # ["my_lambdata"]
)