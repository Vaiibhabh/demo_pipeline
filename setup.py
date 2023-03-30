from setuptools import setup, find_packages

setup(name="census_income",
    version= "0.0.1",
    author="vaibhav",
    author_email= "vjaiswal.vj@gmail.com",
    packages = find_packages(),
    install_requires= ["pandas","numpy","flask"]
    #suppoose so many packages are there then you can create fucntions
    )