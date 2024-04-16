const express = require('express');
const app = express();
const PORT = 3000;

// Обработчик для корневого пути
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

// Обработчик для поиска
app.get('/search', (req, res) => {
  // Получаем значение параметра q из запроса
  const query = req.query.q;

  // Имитируем базу данных книг
  const booksDatabase = {
    "Рей Брэдбери": ["Книга 1", "Книга 2", "Книга 3"],
    // Добавьте другие авторы и их книги по аналогии
  };

  // Проверяем, есть ли книги для введенного автора
  const books = booksDatabase[query];

  // Формируем HTML для результатов поиска
  let resultHTML = '<h2>Search Results:</h2>';
  if (books && books.length > 0) {
    resultHTML += '<ul>';
    books.forEach(book => {
      resultHTML += `<li>${book}</li>`;
    });
    resultHTML += '</ul>';
  } else {
    resultHTML += `<p>Результат поиска "${query}" не найден.</p>`;
  }

  // Отправляем полную HTML страницу с результатами поиска
  const fullHTML = `
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>XSS Demo</title>
        
    <style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f0f0f0;
    }
    
    h1 {
        text-align: center;
        color: #333;
    }
    
    form {
        text-align: center;
        margin-top: 20px;
    }
    
    label {
        font-weight: bold;
    }
    
    input[type="text"] {
        padding: 8px;
        border-radius: 4px;
        border: 1px solid #ccc;
    }
    
    button {
        padding: 8px 16px;
        border-radius: 4px;
        background-color: #007bff;
        color: #fff;
        border: none;
        cursor: pointer;
    }
    
    button:hover {
        background-color: #0056b3;
    }
    
    button:active {
        background-color: #004080;
    }
    
</style>
    </head>
    <body>
        <h1>XSS Demo</h1>
        <h1>книжный магазин</h1>
        <form action="/search" method="GET">
            <label for="query">Search:</label>
            <input type="text" id="query" name="q" value="${query}">
            <button type="submit">Search</button>
        </form>
        ${resultHTML}
    </body>
    </html>
  `;

  res.send(fullHTML);
});

// Запуск сервера
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
