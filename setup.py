import setuptools

with open("README.md", "r") as f:
    desc = f.read()
setuptools.setup(
    name="roblox.py",
    packages=setuptools.find_packages(),
    include_package_data=True,
    version="0.2.4",
    license="MIT",
    description="Modern async API wrapper for Roblox with game client support",
    long_description=desc,
    project_urls={
        "Discord": "https://discord.com/invite/vpEv3HJ",
        "Issue Tracker": "https://github.com/KILR007/roblox.py/issues",
        "GitHub": "https://github.com/KILR007/roblox.py",
        "Examples": "https://github.com/KILR007/roblox.py/tree/master/Examples"},
    long_description_content_type="text/markdown",
    author="KILR",
    url="https://github.com/KILR007/roblox.py",
    keywords=[
        "roblox",
        "roblox api",
        "roblox wrapper",
        "roblox api wrapper",
        'roblox game client',
        'roblox.py'],
    install_requires=["aiohttp"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'],
    python_requires='>=3.7')
