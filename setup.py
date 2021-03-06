from setuptools import setup, find_packages

setup(
    name="vipy",
    version="0.0.3",
    description="Simulate radio interferometer observations and visibility generation.",
    url="https://github.com/radionets-project/vipy",
    author="Kevin Schmidt, Felix Geyer, Stefan Fröse",
    author_email="kevin3.schmidt@tu-dortmund.de",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "astropy",
        "matplotlib",
        "ipython",
        "scipy",
        "pandas",
        "toml",
        "pytest",
        "pytest-cov",
        "jupyter",
        "astroplan",
        "torch",
        "tqdm",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
)
