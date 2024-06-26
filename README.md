# Book Management System

A FastAPI application for managing a collection of books using PostgreSQL.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Database Setup](#database-setup)


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/devikaa002/book-management-using-FastAPI.git
   cd book-management-using-FastAPI

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt

3. Install and configure PostgreSQL. Ensure the database is created and accessible.

## Usage
Start the FastAPI server using uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
Access the API documentation at http://127.0.0.1:8000/docs.

## Database Setup
1. Install PostgreSQL and create a database named apitest.
2. Create a table with the following structure:
```sql
CREATE TABLE book (
    book_id integer NOT NULL,
    title text,
    author text,
    genre text,
    publisher text,
    price integer,
    CONSTRAINT book_pkey PRIMARY KEY (book_id)
);
```
