from setuptools import find_packages, setup

setup(
    name='awsglue',
    version='0.0.1',
    long_description=__doc__,
    packages=find_packages(where="awsglue"),
    package_dir={"": "awsglue"}
    include_package_data=True,
    zip_safe=False,
)
