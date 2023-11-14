from pprint import pprint; import IPython
import chromadb

client = chromadb.HttpClient(host="localhost", port=8000)

# list all collections
client.list_collections()

# make a new collection
collection = client.create_collection("testname")

# get an existing collection
collection = client.get_collection("testname")

# get a collection or create if it doesn't exist already
collection = client.get_or_create_collection("testname")

# delete a collection
# client.delete_collection("testname")

IPython.embed()
