from flask import request, send_file
from flask_restx import Namespace, Resource

from helpers.decorators import auth_required
from services import files_service
from tables import Files

files_namespace: Namespace = Namespace('api/record')


@files_namespace.route('/')
class File(Resource):

    def get(self) -> send_file:
        data: dict = dict(request.args)
        record_data = files_service.file_download(record_id=data.get('id'), user_id=data.get('user'))
        return send_file(record_data.get('file'), as_attachment=True,
                         download_name=f"{record_data.get('filename')}.mp3")

    @auth_required
    def post(self):
        data: dict = dict(file=request.files.get('file'),
                          user_uuid=request.form.get('user_uuid'),
                          user_id=int(request.form.get('user_id')))
        file_uuid: str = files_service.generate_uuid()
        file_data: bytes = files_service.convert_format(data.get('file'))
        file_instance: Files = files_service.add_file_to_db(file_uuid, file_data, data.get('user_id'))
        download_url: str = files_service.make_url(record_id=file_instance.id, user_id=data.get('user_id'))
        return download_url, 200
