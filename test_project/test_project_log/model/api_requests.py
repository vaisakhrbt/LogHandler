
from test_project_log_db import TestProjectLogDB

class ApiRequests(TestProjectLogDB):
	def __init__(self, **kwargs):
		self.requestURL = kwargs.get('requestURL')
		self.parameters = kwargs.get('parameters',)
		self.result = kwargs.get('result')
		self.errorcode = kwargs.get('errorcode')
		self.errormessage = kwargs.get('errormessage')
		self.accessedby = kwargs.get('accessedby')
		self.createdon = kwargs.get('createdon')
		super(ApiRequests, self).__init__()

	@classmethod
	def get_fields(cls):
		return [
			cls.doc_id_name,
			'type',
			'requestURL',
			'parameters',
			'result',
			'errorcode',
			'errormessage',
			'accessedby',
			'createdon',
		]