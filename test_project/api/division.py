from flask import Flask, Blueprint, request, jsonify, abort

from test_project_log.test_project_log import TestProjectLog

from api_helper.api_response import ApiResponse
from api_helper.api_error import ApiError

division_api = Blueprint('division', __name__)


# Test the user api
"""
Request:
{
	"numerator": 1,
	"denominator": 2
}

Response:
{
 "payload": {},
 "sucecss": true
}
"""
@division_api.route('/division_api', methods=['POST'])
def test_hello_api():
	result = ApiResponse.failure(errorName='UnexpectedError')
	if request.method == 'POST':
		try:
			request_json = request.get_json(force=True)
			numerator = request_json['numerator']
			denominator = request_json['denominator']

		except Exception as e:
			return abort(400, ApiError.InputNotValid)		

		try:
			if type(numerator) not in [int, float] or type(denominator) not in [int, float]:
				result = ApiResponse.failure(errorName='InputNotValid')
			else:
				result = ApiResponse.success()
				div_result = numerator/denominator
				result_dict = {
					'numerator': numerator,
					'denominator': denominator,
					'output': div_result
				}
				if div_result == numerator/float(denominator):
					result = ApiResponse.success(result=result_dict)

				else:
					result = ApiResponse.success(result=result_dict, messageName='IntegierDivision')

		except ZeroDivisionError as e:
			TestProjectLog().addExceptions(e)
			result = ApiResponse.failure(errorName='ZeroDivision')

		except Exception as e:
			TestProjectLog().addExceptions(e)
			result = ApiResponse.failure(errorName='UnexpectedError')
	else:
		result = ApiResponse.failure(errorName='UndefinedRequest')

	TestProjectLog().addApiRequests(request, result)
	return jsonify(result)
