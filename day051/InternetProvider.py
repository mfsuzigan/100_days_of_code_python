class InternetProvider:

    def __init__(self, name, min_download_speed, min_upload_speed):
        self.name = name
        self.min_download_speed = min_download_speed
        self.min_upload_speed = min_upload_speed
