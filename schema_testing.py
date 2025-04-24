import time
import datetime
import json
from pymongo import MongoClient

URI = "mongodb+srv://test:12345@cluster0.oj09f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
BATCH_SIZE = 10000

def get_collection():
    client = MongoClient(URI)
    db = client.final
    return client, db.person

simple_schema =  {
                "id": "0",
                "first_name": "John",
                "last_name": "Doe",
                "age": "30",
                "gender": "Male",
                "phone": "123456789",
                "zip_code": "90001",
                "date_of_birth": "1990-01-01",
                "language": "English",
                "hobby": "reading"
            }
moderate_schema = {
                "id": "0",
                "first_name": "John",
                "last_name": "Doe",
                "age": "30",
                "gender": "Male",
                "phone": "123456789",
                "address": {
                    "zip_code": "90001",
                    "street": "125 ravenridge road",
                    "house_number": "55",
                    "city": "Calgary",
                    "state": "Alberta",
                    "country": "Canada"
                },
                "date_of_birth": {
                    "year": "2001",
                    "month": "February",
                    "day": "11"
                },
                "language": "English",
                "hobby": "Reading",
                "employment": {
                    "job": "Software Engineer",
                    "years_of_experience": "2",
                    "company": "Google",
                    "salary": "100000"
                }
            }

complex_schema = {
                "id": "0",
                "first_name": "John",
                "last_name": "Doe",
                "age": "30",
                "gender": "Male",
                "phone": "123456789",
                "address": {
                    "zip_code": "90001",
                    "street": {
                        "full_street_name": "125 ravenridge road",
                        "year_built": "2002",
                        "has_intersection": "no",
                        "school": "ravenridge high school"
                    },
                    "house_number": "55",
                    "city": "Calgary",
                    "state": "Alberta",
                    "country": "Canada"
                },
                "date_of_birth": {
                    "year": "2001",
                    "month": "February",
                    "day": "11"
                },
                "language": "English",
                "hobby": "Reading",
                "employment": {
                    "job": "Software Engineer",
                    "years_of_experience": "2",
                    "company": {
                        "company_name": "Google",
                        "num_employees": "100000",
                        "industry": "technology",
                        "founder": "larry page"
                    },
                    "salary": "100000"
                }
            }

def create():  
    client, collection = get_collection()

    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    batch = []  # This will store the documents to be inserted

    for _ in range(50):
        for i in range(BATCH_SIZE):  
            person = {
                "id": str(i),
                "first_name": "John",
                "last_name": "Doe",
                "age": "30",
                "gender": "Male",
                "phone": "123456789",
                "address": {
                    "zip_code": "90001",
                    "street": {
                        "full_street_name": "125 ravenridge road",
                        "year_built": "2002",
                        "has_intersection": "no",
                        "school": "ravenridge high school"
                    },
                    "house_number": "55",
                    "city": "Calgary",
                    "state": "Alberta",
                    "country": "Canada"
                },
                "date_of_birth": {
                    "year": "2001",
                    "month": "February",
                    "day": "11"
                },
                "language": "English",
                "hobby": "Reading",
                "employment": {
                    "job": "Software Engineer",
                    "years_of_experience": "2",
                    "company": {
                        "company_name": "Google",
                        "num_employees": "100000",
                        "industry": "technology",
                        "founder": "larry page"
                    },
                    "salary": "100000"
                }
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

def main():
    create()
    read_documents()
    update_field()
    delete_all()


if __name__ == "__main__":
    main()