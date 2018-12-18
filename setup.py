from setuptools import setup

description = """
Redis-cluster plugin for Django
"""

setup(
    name="dedis-cluster",
    url="https://github.com/feiwencaho/dedis-cluster.git",
    author="feivincent",
    author_email="hi@feiwenchao.me",
    version="1.0.0",
    packages=[
        "dedis_cluster",
        "dedis_cluster.client",
        "dedis_cluster.serializers",
        "dedis_cluster.compressors",
    ],
    description=description.strip(),
    install_requires=[
        "Django>=1.9.6",
        "redis>=2.10.5",
        "redis-py-cluster>=1.2.0",
        "msgpack-python>=0.4.7",
    ],
    zip_safe=False,
    include_package_data=True,
    package_data={
        "": ["*.html"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)
