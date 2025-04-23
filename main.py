from pymongo import MongoClient
from schema import StringDataPerson
from pymongo.mongo_client import MongoClient
from bson import ObjectId
import json
import time
import datetime


def create():
    URI = "mongodb+srv://test:12345@cluster0.oj09f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(URI)
    db = client.final
    collection = db.person

    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


    batch_size = 10000  # Define the batch size
    batch = []  # This will store the documents to be inserted

    for _ in range(10):
        for i in range(batch_size):    
            person = {
                "id": str(i),
                "first_name": "John",
                "last_name": "Doe",
                "age": "30",
                "gender": "Male",
                "phone": "123456789",
                "zip_code": "90001",
                "date_of_birth": "1990-01-01",
                "language": "English",
                "hobby": "Reading",
            }

            batch.append(person)

        if len(batch) >= batch_size:
            try:
                start_time = time.time()
                collection.insert_many(batch)
                print(datetime.datetime.now())
                total_time = time.time() - start_time
                print(f"Operation took {total_time}")
                print(f"Inserted {len(batch)} documents.")
                batch.clear()  
            except Exception as e:
                print(f"Error saving batch: {e}")

        else:
            try:
                collection.insert_many(batch)
                print(f"Inserted remaining {len(batch)} documents.")
            except Exception as e:
                print(f"Error saving remaining documents: {e}")

def delete_all():
    URI = "mongodb+srv://test:12345@cluster0.oj09f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(URI)
    db = client.final
    collection = db.person

    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
        return

    try:
        start_time = time.time()
        print(datetime.datetime.now())

        result = collection.delete_many({})  # Deletes all documents
        end_time = time.time()

        print(f"Deleted {result.deleted_count} documents.")
        print(f"Operation took {end_time - start_time} seconds.")
    except Exception as e:
        print(f"Error deleting documents: {e}")

def update_field():
    URI = "mongodb+srv://test:12345@cluster0.oj09f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(URI)
    db = client.final
    collection = db.person

    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
        return

    try:
        start_time = time.time()
        print(datetime.datetime.now())


        # Change the value of the 'gender' field (for example, setting it to a new value)
        result = collection.update_many(
            {},  # Filter to select all documents (use a condition here if you want to update specific documents)
            {"$set": {"hobby": "painting"}}  # Update operation: setting the 'hobby' field to "reading"
        )

        end_time = time.time()

        print(f"Updated {result.modified_count} documents.")
        print(f"Operation took {end_time - start_time} seconds.")

    except Exception as e:
        print(f"Error updating documents: {e}")


def read_documents():
    URI = "mongodb+srv://test:12345@cluster0.oj09f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(URI)
    db = client.final
    collection = db.person

    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
        return

    try:
        start_time = time.time()

        batch_size = 10000
        total_documents = 0

        # Use a cursor to read documents in batches
        cursor = collection.find({}).batch_size(batch_size)

        for batch in cursor:
            total_documents += 1  # count each document

        end_time = time.time()

        print(datetime.datetime.now())
        print(f"Read {total_documents} documents.")
        print(f"Operation took {end_time - start_time} seconds.")
    except Exception as e:
        print(f"Error reading documents: {e}")


if __name__ == "__main__":
    create()
