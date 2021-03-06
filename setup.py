from setuptools import setup

url = ""
version = "0.1.0"
readme = open('README.md').read()

# Note:  psutil is needed for demo purposes only.

setup(
    name="test_proxy_client",
    packages=["test_proxy_client"],
    version=version,
    description="Tools for drawing 2d and 3d interactive visualizations using Jupyter proxy widgets",
    long_description=readme,
    include_package_data=True,
    author="Aaron Watters",
    author_email="awatters@flatironinstitute.org",
    url=url,
    install_requires=[
        "jp_proxy_widget", 
        ],
    license="MIT"
)
