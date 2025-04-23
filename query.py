from pymongo import MongoClient
from schema import StringDataPerson, Transactions, CurrencyEnum, TransactionTypeEnum, StatusEnum
from pymongo.mongo_client import MongoClient
from bson import ObjectId
import time

def main():
    URI = "mongodb+srv://test:12345@cluster0.oj09f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(URI)
    db = client.final
    collection = db.person

    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


    for i in range(5):
        person = StringDataPerson(
            id=str(i),
            first_name="John",
            last_name="Doe",
            age="30",  
            gender="Male",
            email="john.doe@example.com",
            phone="1234567890",
            street="123 Elm St.",
            city="Somewhere",
            state="CA",
            zip_code="90001",
            date_of_birth="1990-01-01",
            occupation="Engineer",
            company="Tech Corp",
            marital_status="Single",
            nationality="American",
            language="English",
            hobby="Reading",
            last_updated="2025-03-22"
        )
        
        try:
            # Insert
            collection.insert_one(person.model_dump(by_alias=True))
            print("Person saved successfully!")
        except Exception as e:
            print(f"Error saving person: {e}")
    
    try:
        # Select
        all_person = collection.find({})
        print(all_person)
    except Exception as e:
        print(f"Error select person: {e}")

    
    for i in range(5):
        transaction = Transactions(
        id=str(1),
        person_id=str(1),
        amount = 100.00,
        currency = CurrencyEnum.CAD.value,
        transaction_type = TransactionTypeEnum.purchase.value,
        status = StatusEnum.pending.value,
        timestamp = time.time()
        )
        
        try:
            # Insert
            collection.insert_one(transaction.model_dump(by_alias=True))
            print("Transaction saved successfully!")
        except Exception as e:
            print(f"Error saving transaction: {e}")
    
    try:
        # Join
        all_person = collection.find({})
        print(all_person)
    except Exception as e:
        print(f"Error select person: {e}")
    
    



if __name__ == "__main__":
    main()

    
