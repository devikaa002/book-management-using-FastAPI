from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2

app = FastAPI()
data = []

db_name = "apitest"
db_user = "postgres"
db_pass = "password"
db_host = "localhost"
db_port = "5432"


conn = psycopg2.connect(
    dbname = db_name,
    user = db_user,
    password = db_pass,
    host = db_host,
    port = db_port
)


# Base class
class Book(BaseModel):
    book_id: int
    title: str
    author: str
    genre: str
    publisher: str
    price: int

# To insert book
@app.post("/book")
def add_new_book(book: Book):
    data.append(book.dict())
    cursor = conn.cursor()
    insert_query = "INSERT INTO book (book_id,title,author,genre,publisher,price) VALUES (%s,%s,%s,%s,%s,%s)"
    cursor.execute(insert_query,(book.book_id,book.title,book.author,book.genre,book.publisher,book.price))
    conn.commit()
    cursor.close()


    #to fetch books and show in list.
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book")
    books = cursor.fetchall()
    cursor.close()
    return{"books":books}


#fetch book details in same genre
@app.get("/book/{genre}")
def fetch_book_details(genre: str):
    cursor = conn.cursor()
    select_query = "SELECT * FROM book WHERE LOWER(genre) = LOWER(%s)"
    cursor.execute(select_query, (genre,))
    books = cursor.fetchall()
    cursor.close()
    if not books:
        raise HTTPException(status_code=404, detail="Books not found for the given genre")
    return books


#update book details based on its book_id
@app.put("/book/{book_id}")
def update_book_details(book_id: int, title: str, author: str, genre: str, publisher: str, price: int):
    cursor = conn.cursor()
    update_query = "UPDATE book SET title = %s, author = %s, genre = %s, publisher = %s, price = %s WHERE book_id = %s"
    cursor.execute(update_query, (title,author,genre,publisher,price,book_id))
    conn.commit()
    cursor.close()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Book not found")

    # Fetch the updated book details
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book WHERE book_id = %s", (book_id,))
    updated_book = cursor.fetchone()
    cursor.close()
    return {"book": updated_book}


#delete book with its book_id
@app.delete("/book/{book_id}")
def delete_book_record(book_id: int):
    cursor = conn.cursor()
    delete_query = "DELETE FROM book WHERE book_id = %s"
    cursor.execute(delete_query, (book_id,))
    conn.commit()
    cursor.close()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Record deleted successfully."}
