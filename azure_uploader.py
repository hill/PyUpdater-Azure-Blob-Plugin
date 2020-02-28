from pyupdater.core.uploader import BaseUploader


class MyUploader(BaseUploader):

    name = "my uploader"
    author = "Jane Doe"

    def init_config(self, config):
        self.server_url = config["server_url"]

    def set_config(self, config):
        server_name = self.get_answer("Please enter server name\n--> ")
        config["server_url"] = server_name

    def upload_file(self, filename):
        # Make the magic happen
        files = {"file": open(filename, "rb")}
        r = request.post(self.server_url, files=files)
