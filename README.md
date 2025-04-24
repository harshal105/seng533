# Comprehensive Review of MongoDB Performance

## Overview
MongoDB is a widely-used NoSQL database known for its scalability, flexibility, and support for modern application development.  
This project conducts a comprehensive performance evaluation of MongoDB under varying conditions, focusing on:

- **Data Types**
- **Workload Size**
- **Concurrency**
- **Schema Complexity**

## Performance Analysis
The analysis is conducted using four Python scripts, each targeting one of the test variables. The following performance metrics are tracked:

- **Internal Requests**
- **Network In**
- **Network Out**
- **Latency**
- **Processed Throughput**

---

## 🔧 Test Variables

### Workload Size
Three data volumes are used to test scalability:

- `100,000` entries  
- `500,000` entries  
- `1,000,000` entries

### Data Types
Two data-type configurations are tested:

- All fields as **strings**
- A mix of **strings**, **integers**, and **arrays**

### Schema Types
Three schema structures of increasing complexity:

1. **Flat schema**
2. **Moderately nested schema**
3. **Complex nested schema**

### Concurrency
Tests simulate concurrent operations using:

- `1` thread  
- `2` threads  
- `5` threads

---

## File Structure

- `workload_test.py` — Analyzes performance under different data volumes  
- `datatype_test.py` — Compares schema with varying data types  
- `schema_test.py` — Tests performance with different schema complexities  
- `concurrency_test.py` — Evaluates performance under concurrent operations  

---

