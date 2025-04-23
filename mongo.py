from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

URI = "mongodb+srv://test:12345@cluster0.oj09f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(URI)
db = client.final
collection = db.person

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")

    # Select All Person
    all_person = collection.find({})

    
except Exception as e:
    print(e)