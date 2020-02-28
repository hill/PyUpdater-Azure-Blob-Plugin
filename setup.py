from setuptools import setup

setup(
    name="PyUpdater-Azure-Blob-Plugin",
    description="Azure Blob Storage plugin for PyUpdater",
    author="Tom Hill",
    author_email="tom@hill.xyz",
    provides=["pyupdater.plugins",],
    entry_points={"pyupdater.plugins": ["my_uploader = my_uploader:MyUploader",]},
)
