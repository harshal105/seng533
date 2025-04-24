import json
import time
import datetime
from pymongo import MongoClient


URI = "mongodb+srv://test:12345@cluster0.oj09f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

BATCH_SIZE = 10000
SMALL_WORKLOAD_SIZE = 10
MEDIUM_WORKLOAD_SIZE = 50
LARGE_WORKLOAD_SIZE = 100

def get_collection():
    client = MongoClient(URI)
    db = client.final
    return client, db.person


def create():
    client, collection = get_collection()

    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


    batch = []  # This will store the documents to be inserted

    for _ in range(SMALL_WORKLOAD_SIZE):
        for i in range(BATCH_SIZE):    
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

        if len(batch) >= BATCH_SIZE:
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
    client, collection = get_collection()

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
    client, collection = get_collection()

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
    client, collection = get_collection()

    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
        return

    try:
        start_time = time.time()

        total_documents = 0

        # Use a cursor to read documents in batches
        cursor = collection.find({}).batch_size(BATCH_SIZE)

        for batch in cursor:
            total_documents += 1  # count each document

        end_time = time.time()

        print(datetime.datetime.now())
        print(f"Read {total_documents} documents.")
        print(f"Operation took {end_time - start_time} seconds.")
    except Exception as e:
        print(f"Error reading documents: {e}")


def main():
    create()
    read_documents()
    update_field()
    delete_all()

if __name__ == "__main__":
    main()
