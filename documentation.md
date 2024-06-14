## Add Book
Input: book name, author, genre, publisher, and price
Output: list of added books with all the entered details
URL: /book
Method: POST
Request Body:
```json
{
  "book_id": 2,
  "title": "The God of Small Things",
  "author": "Arundhati Roy",
  "genre": "Fiction",
  "publisher": "IndiaInk",
  "price": 500
}
```

Response:
```json
{
  "books": [
    [
      1,
      "Gitanjali",
      "Rabindranath Tagore",
      "Poem",
      "Macmillan and Company",
      123
    ],
    [
      2,
      "The God of Small Things",
      "Arundhati Roy",
      "Fiction",
      "IndiaInk",
      500
    ]
  ]
}
```


## Fetch book details
Input: genre
Output: a list of all the books that belong to the genre provided in the input
URL: /book/{genre}
Method: GET
Response:
```json
[
  [
    2,
    "The God of Small Things",
    "Arundhati Roy",
    "Fiction",
    "IndiaInk",
    500
  ],
  [
    4,
    "A Suitable Boy",
    "Vikram Seth",
    "Fiction",
    "HarperCollins",
    700
  ]
]
```

## Update book details
Input: book_id, book name, author, genre, publisher, price
Output: display all the updated information for the given book
URL: /book/{book_id}
Method: PUT
Response:
```json
{
  "book": [
    1,
    "Interpreter of Maladies",
    "Jhumpa Lahiri",
    "Short Stories",
    "Houghton Mifflin Harcourt",
    400
  ]
}
```

## Delete a Book
Input: book_id
Output: a success message indicating that the book has been deleted
URL: /book/{book_id}
Method: DELETE
Response:
```json
{
  "message": "Record deleted successfully."
}
```
