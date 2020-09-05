import setuptools

with open("README.md","r") as f:
	desc = f.read()

setuptools.setup(
name = "pyrblx",
packages = setuptools.find_packages(),
include_package_data=True,
version = "3.0",
license = "MIT",
description = "pyrblx Is A library Written In Python For Roblox",
long_description = desc,
long_description_content_type="text/markdown",
author = "KILR",
author_email = "abstractwilliam0@gmail.com",
url = "https://github.com/KILR007/pyrblx",
keywords = ["roblox"],
install_requires = ["requests"],
classifiers = [
'License :: OSI Approved :: MIT License',
'Programming Language :: Python :: 3',
'Operating System :: OS Independent'
],
python_requires='>=3.6'
)
