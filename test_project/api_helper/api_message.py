class ApiMessage:


	Messages = {
		'UndefinedMessage'					: {600: "Undefined Message."},
		'IntegierDivision'					: {600100: "By default Integer Division Support Only. Use float to get more precision."},
	}

	@classmethod
	def get_message(cls, msg_name):
		message = cls.Messages.get(msg_name, {}).items()
		if len(message):
			return { 
				'code': message[0][0],
				'message': message[0][1]
			}
		else:
			return cls.get_message('UndefinedMessage')
