class ApiError:

	Success = 'Success'
	Failure = 'Failure'
	InputNotValid = "Input validation issues"

	Errors = {
		'SomethingWrong'			: {500: "Something went wrong!"},
		'UndefinedError'			: {500000: "Undefined Error."},
		'UnexpectedError'			: {500100: "We are unable to serve you right now. Kindly try again after sometime."},

		'UndefinedRequest'			: {400: "Unsupported Request."},
		'ZeroDivision'				: {400100: "Division by zero is not defined."},
		
		# 'InvalidData'				: {'1017': "Invalid data recieved"},
		# 'UnAuthorizedAccess'		: {'1020': "Token Invalid."},
	}

	@classmethod
	def getError(cls, error_name):
		error = cls.Errors.get(error_name, {}).items()
		if len(error):
			return { 
				'code': error[0][0],
				'message': error[0][1]
			}
		else:
			return cls.getError('UndefinedError')
