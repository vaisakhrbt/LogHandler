import time
import uuid

from test_project_log_db import TestProjectLogDB

class Exceptions(TestProjectLogDB):
	def __init__(self, **kwargs):
		self.stacktrace = kwargs.get('stacktrace')
		self.user = kwargs.get('user')
		self.linenumber = kwargs.get('linenumber')
		self.exceptionmessage = kwargs.get('exceptionmessage')
		self.createdon = kwargs.get('createdon', time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
		super(Exceptions, self).__init__()

	@classmethod
	def get_fields(cls):
		return [
			cls.doc_id_name,
			'type',
			'user',
			'stacktrace',
			'linenumber',
			'exceptionmessage',
			'createdon',
		]