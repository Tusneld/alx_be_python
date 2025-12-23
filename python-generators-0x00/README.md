# Python Generators Project

## About the Project
This project explores advanced usage of **Python Generators** to handle large datasets efficiently. By leveraging the `yield` keyword, these scripts demonstrate how to process data from a MySQL database using minimal memory, implementing batch processing, lazy loading, and real-time data streaming.

## Learning Objectives
* **Master Python Generators:** Learn to use `yield` for iterative data processing.
* **Memory Efficiency:** Handle large datasets without overloading system RAM.
* **Batch Processing:** Implement logic to fetch and process data in manageable chunks.
* **Lazy Loading:** Simulate paginated data retrieval.
* **Database Integration:** Connect Python generators with SQL databases (MySQL).

## Requirements
* **Python 3.x**
* **MySQL Server**
* **Python Libraries:** `mysql-connector-python`

## Project Structure

| File | Description |
| --- | --- |
| `seed.py` | Sets up the `ALX_prodev` database and populates the `user_data` table from a CSV. |
| `0-stream_users.py` | Contains a generator that streams user rows one by one. |
| `1-batch_processing.py` | Fetches data in batches and filters users over age 25. |
| `2-lazy_paginate.py` | Uses a generator to lazily load paginated data from the database. |
| `4-stream_ages.py` | Computes the average age of users using a memory-efficient generator. |

## How to Run
1.  **Set up the database:**
    Update the credentials in `seed.py` and run:
    ```bash
    python3 seed.py
    ```
2.  **Test a specific task:**
    For example, to test the average age calculation:
    ```bash
    python3 4-stream_ages.py
    ```