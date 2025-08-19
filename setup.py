from setuptools import setup, find_packages

setup(
    name="pypi-workspace-test",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
        "vulnerable-root-package>=1.0.0",
        "missing-root-lib>=2.1.0"
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "phantom-root-dev-tool>=1.0.0"
        ]
    }
)
