from setuptools import setup, find_packages

setup(
    name="turbo",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["numpy",
                      "matplotlib",
                      "scipy",
                      "ax-platform>=0.1.17",
                      "cma == 2.7.0",
                      "dragonfly-opt == 0.1.4",
                      "smac==0.11.1"],
)
