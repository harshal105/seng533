



moderate_schema = {
                "id": str(i),
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
                        "has_intersection": "no"
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
                    }
                    "salary": "100000"
                }
            }