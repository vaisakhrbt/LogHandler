import time
import uuid
from couchbase.bucket import Bucket


from config import Config
from model.couchbase_model import CouchbaseModel

#@TODO: Apply DB operations asynchronously
class TestProjectLogDB(CouchbaseModel):
	def __init__(self, **kwargs):
		super(TestProjectLogDB, self).__init__()

	@classmethod
	def get_client(cls):
		return super(TestProjectLogDB, cls).get_client(bucket_name=Config.couchbase_bucket_for_logs)
