import io
import uuid
from dataclasses import dataclass

from pydub import AudioSegment

from repositories import files_repository, FilesRepo
from urllib.parse import urlencode

from settings import BASE_FILE_URL
from tables import Files


@dataclass
class FilesService:
    repository: FilesRepo = files_repository

    def convert_format(self, file):
        try:
            audio_bytes = file.read()
            audio = AudioSegment.from_file(io.BytesIO(audio_bytes))
            audio = audio.export(format='mp3')
            mp3_data = audio.read()
        except Exception as e:
            return {'message': "Convert failed", 'status_code': 500}
        return mp3_data

    def generate_uuid(self):
        new_uuid = uuid.uuid4()
        return new_uuid

    def add_file_to_db(self, file_uuid, file_data, user_id):
        instance = self.repository.create(file_uuid=file_uuid,
                                          file_data=file_data,
                                          user_id=user_id)
        return instance

    def make_url(self, record_id, user_id):
        query_params = {'id': record_id, 'user': user_id}
        query_string = urlencode(query_params)
        url = f'{BASE_FILE_URL}?{query_string}'
        return url

    def file_download(self, record_id, user_id):
        record: Files = self.repository.get_first_by_values(id=record_id, user_id=user_id)[0]
        record_bytes: bytes = record.file_data
        filename: str = record.file_uuid
        record_to_push = io.BytesIO(record_bytes)
        data = dict(
            file=record_to_push,
            filename=filename
        )
        return data
