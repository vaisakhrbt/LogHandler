import sys
import traceback

from model import ApiRequests as ApiRequestsLogs
from model import Exceptions as ExceptionsLogs

from config import Config

class TestProjectLog(object):
	def __init__(self):
		pass

	def addApiRequests(self, request, result, user=None):
		if Config.logging_mode is False:
			return

		logs = ApiRequestsLogs()
		logs.accessedby = user
		logs.requestURL = str(request.environ['PATH_INFO'])
		try:
			logs.parameters = request.get_json(force=True)
		except Exception as e:
			# Handle error when no data field passed
			logs.parameters = {}
		logs.result = result
		error = result.get('error')
		if result.get('success') is False and error:
			logs.errorcode = error.get('code')
			logs.errormessage = error.get('message')
		return logs.insert()

	def addExceptions(self, exception, user=None):
		if Config.logging_mode is False:
			return

		logs = ExceptionsLogs()
		logs.user = user
		logs.stacktrace = traceback.format_exc()
		logs.linenumber = sys.exc_info()[2].tb_lineno
		logs.exceptionmessage = str(exception)
		return logs.insert()
