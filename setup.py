from setuptools import setup, find_packages

with open('requirements.txt') as f:
	required = f.read().splitlines()

setup(
    name="user_api",
    version="0.1.0",
    description="Example User REST API",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Egor Berdovskiy",
    author_email="lotus9200@gmail.com",
    url="https://github.com/yeegie/user_rest_api",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=required
)
