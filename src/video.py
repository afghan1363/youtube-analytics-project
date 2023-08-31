import json
import os
from googleapiclient.discovery import build


class Video:
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        try:
            self.video_id = video_id
            self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                             id=video_id).execute()
            self.title: str = self.video_response['items'][0]['snippet']['title']
            self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']
            self.comment_count: int = self.video_response['items'][0]['statistics']['commentCount']
            self.url: str = f'https://www.youtube.com/watch?v={self.video_id}'
        except IndexError:
            self.title = None
            self.view_count = None
            self.like_count = None
            self.comment_count = None
            self.url = None

    def __str__(self):
        return self.title

    def print_info(self) -> None:
        """Выводит в консоль информацию о видео. Вставил для экспериментов"""
        dict_to_print = self.video_response
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


class PLVideo(Video):

    def __init__(self, video_id, pls_id):
        super().__init__(video_id)
        self.pls_id = pls_id


if __name__ == "__main__":
    video1 = Video('AWX4JnAnjBE')
    video1.print_info()
