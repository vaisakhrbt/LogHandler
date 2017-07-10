import uuid, time, json
from couchbase.bucket import Bucket
from couchbase.n1ql import N1QLQuery
from couchbase.exceptions import NotFoundError


from config import Config

def get_err_message(e):
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	errTuple = (exc_type, fname, exc_tb.tb_lineno, str(e))
	current_app.logger.error(str(errTuple))
	return 'Error: ' + str(errTuple)

class CouchbaseModel(object):

	_clients = dict()

	type = None
	doc_id_name = '_uuid'

	def __init__(self):
		self.type = self.get_type()

	@classmethod
	def get_client(cls, bucket_name=None):
		bucket_name = bucket_name if bucket_name else Config.couchbase_bucket
		if cls._clients.get(bucket_name) is None:
			cls._clients[bucket_name] = Bucket("couchbase://{}/{}".format(Config.couchbase_ip, bucket_name))
		return cls._clients[bucket_name]

	@staticmethod
	def get_uuid():
		return str(uuid.uuid4())

	@classmethod
	def get_fields(cls):
		raise NotImplementedError

	@classmethod
	def get_type(cls):
		return cls.__name__.lower()

	def get_data(self):
		data = dict()
		for key in self.get_fields():
			data[key] = getattr(self, key, None)
		try:
			# To handled nested data structure
			return json.loads(json.dumps(data))
		except Exception as e:
			print "Data error: " + str(e)
			return False

	def set_data(self, data):
		try:
			for key in self.get_fields():
				if key in data:
					setattr(self, key, data.get(key))
			return True
		except Exception as e:
			return False

	def get_document_name(self):
		doc_id = getattr(self, self.doc_id_name, None)
		if doc_id is None:
			raise NameError("Document Name not provided")
		return "{}::{}".format(self.get_type(), doc_id)


	def find(self, doc_name=None):
		cb = self.get_client()
		doc_name = self.get_document_name() if doc_name is None else doc_name
		try:
			data = cb.get(doc_name)
			self.set_data(data.value)
			return self.get_data()
		except NotFoundError as e:
			get_err_message(e)
			return False

	def insert(self):
		cb = self.get_client()
		try:
			if(hasattr(self, 'createdon') and not self.createdon):
				self.createdon = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
			if not hasattr(self, self.doc_id_name):
				setattr(self, self.doc_id_name, self.get_uuid())
			cb.insert(self.get_document_name(), self.get_data())
			return True
		except Exception as e:
			get_err_message(e)
			return False

	def update(self, data=None):
		cb = self.get_client()
		doc_name = self.get_document_name()
		if data:
			self.set_data(data)
		try:
			cb.replace(doc_name, self.get_data())
			return True
		except Exception as e:
			get_err_message(e)
			return False

	def save(self):
		cb = self.get_client()
		try:
			cb.upsert(documentId, dataObject)
			return True
		except Exception as e:
			get_err_message(e)
			return False

	def query(self, query_string):
		# Single bucket query
		cb = self.get_client()
		try:
			result = cb.n1ql_query(N1QLQuery(query_string))
			return result
		except Exception as e:
			get_err_message(e)
			return False

	def query_all(self, query_string):
		# Joined bucket query
		pass