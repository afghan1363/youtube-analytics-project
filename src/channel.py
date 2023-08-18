from googleapiclient.discovery import build
import os
import json


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.count_subscribers = self.channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.count_views = self.channel["items"][0]["statistics"]["viewCount"]

    def __str__(self):
        return f"{self.title} ({self.url})"

    @property
    def channel_id(self):
        return self.__channel_id

    # @channel_id.setter
    # def channel_id(self, value):
    #    self.__channel_id = value

    @classmethod
    def get_service(cls):
        return cls.youtube

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self, file_name):
        with open(file_name, "w") as data_file:
            json.dump(self.__dict__, data_file)


    def __add__(self, other):
        return int(self.count_subscribers) + int(other.count_subscribers)

    def __sub__(self, other):
        return int(self.count_subscribers) - int(other.count_subscribers)

    def __lt__(self, other):
        return int(self.count_subscribers) < int(other.count_subscribers)

    def __le__(self, other):
        return self.count_subscribers <= other.count_subscribers

    def __gt__(self, other):
        return int(self.count_subscribers) > int(other.count_subscribers)

    def __ge__(self, other):
        return int(self.count_subscribers) >= int(other.count_subscribers)
