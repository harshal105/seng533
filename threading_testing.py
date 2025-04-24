import threading
import time
import datetime
from pymongo import MongoClient

URI = "mongodb+srv://test:12345@cluster0.oj09f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
BATCH_SIZE = 10000

def get_collection():
    client = MongoClient(URI)
    db = client.final
    return client, db.person

def create():
    client, collection = get_collection()
    try:
        client.admin.command("ping")
        print(f"[{threading.current_thread().name}] Connected to MongoDB.")
    except Exception as e:
        print(e)
        return

    for _ in range(10):
        batch = []
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

        try:
            start_time = time.time()
            print(f"[{threading.current_thread().name}] {datetime.datetime.now()}: Starting {start_time}")
            collection.insert_many(batch)
            print(f"[{threading.current_thread().name}] {datetime.datetime.now()}: Inserted {len(batch)} docs in {time.time() - start_time:.2f} seconds.")
        except Exception as e:
            print(f"Error saving batch: {e}")


def delete_documents(start_index, batch_size):
    client, collection = get_collection()

    try:
        client.admin.command("ping")
        print(f"[{threading.current_thread().name}] Connected to MongoDB.")
    except Exception as e:
        print(e)
        return

    try:
        # Step 1: Get the _ids in the range
        docs = list(collection.find({}).skip(start_index).limit(batch_size))
        ids_to_delete = [doc['_id'] for doc in docs]

        if not ids_to_delete:
            print(f"[{threading.current_thread().name}] No documents to delete.")
            return
        
        # Sleep here so we can check activity spikes on charts
        time.sleep(120)
        # Step 2: Delete documents with those _ids
        start_time = time.time()
        print(f"[{threading.current_thread().name}] {datetime.datetime.now()}: Starting {start_time}")

        result = collection.delete_many({ "_id": { "$in": ids_to_delete } })

        end_time = time.time()
        print(f"[{threading.current_thread().name}] {datetime.datetime.now()}  Deleted {result.deleted_count} documents in {end_time - start_time:.2f} seconds.")
    except Exception as e:
        print(f"Error deleting documents: {e}")



def update_field(start_index, batch_size):
    client, collection = get_collection()

    try:
        client.admin.command("ping")
        print(f"[{threading.current_thread().name}] Connected to MongoDB.")
    except Exception as e:
        print(e)
        return

    try:

        # First, get the _ids of documents in the specified range
        docs = list(collection.find({}).skip(start_index).limit(batch_size))
        ids = [doc['_id'] for doc in docs]
        
        # Sleep here so we can check activity spikes on charts
        time.sleep(120)

        start_time = time.time()
        # Then, update only those documents
        print(f"[{threading.current_thread().name}] {datetime.datetime.now()}: Starting {start_time}")

        result = collection.update_many(
            { "_id": { "$in": ids }},
            { "$set": { "hobby": "skiing" }}
        )
        end_time = time.time()
        print(f"[{threading.current_thread().name}] {datetime.datetime.now()} Updated {result.modified_count} documents in {end_time - start_time:.2f} seconds.")
    except Exception as e:
        print(f"Error updating documents: {e}")



def read_documents(start_index, batch_size):
    client, collection = get_collection()
    try:
        client.admin.command("ping")
        print(f"[{threading.current_thread().name}] Connected to MongoDB.")
    except Exception as e:
        print(e)
        return

    try:
        start_time = time.time()
        print(f"[{threading.current_thread().name}] {datetime.datetime.now()}: Starting {start_time}")
        cursor = collection.find({}).skip(start_index).limit(batch_size)

        count = 0
        for _ in cursor:
            count += 1

        duration = time.time() - start_time
        print(f"[{threading.current_thread().name}] {datetime.datetime.now()} Read {count} docs in {duration:.2f} seconds (from {start_index} to {start_index + batch_size}).")
    except Exception as e:
        print(f"Error reading documents: {e}")



def run_with_threads_create(num_threads):
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=create, name=f"Thread-{i+1}")
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

def run_with_threads_change(operation_func,num_threads):
    total_docs = BATCH_SIZE * 10
    num_threads = 2
    docs_per_thread = total_docs // num_threads

    threads = []
    for i in range(num_threads):
        start = i * docs_per_thread
        t = threading.Thread(
            target=operation_func,
            name=f"Thread-{i+1}",
            args=(start, docs_per_thread)
        )
        t.start()
        threads.append(t)

    for t in threads:
        t.join()        

def main():
    # Choose number of threads: 1, 2, or 5
    num_threads = 2

    run_with_threads_change(delete_documents, num_threads)

    run_with_threads_create(num_threads) 

    run_with_threads_change(update_field, num_threads)

    run_with_threads_change(read_documents, num_threads)

if __name__ == "__main__":
    main()

