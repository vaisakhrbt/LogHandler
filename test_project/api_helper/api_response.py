from api_helper.api_error import ApiError
from api_helper.api_message import ApiMessage


class ApiResponse:

	"""
	Response:
	{
		'success': true,
		'payload': data
	}
	"""
	@classmethod
	def success(cls, result=None, messageName=None):

		result = result if result else {}
		if messageName:
			result.update(ApiMessage.get_message(messageName))
		return {
			'success': True,
			'payload': result
		}

	"""
	Response:
	{
		'success': false,
		'payload': {},
		'error': {
			'code': error_code_number
			'message': error_message
		}
	}
	"""
	@classmethod
	def failure(cls, errorName=None, errorDetails=None):
		# errorDetails not provided get the message by name
		error_details = errorDetails if errorDetails else ApiError.getError(errorName)
		return {
				'success': False,
				'error': error_details,
				'payload': {}
			}
