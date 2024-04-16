const http = require('http');
const cors = require('cors');
const server = http.createServer((req, res) => {
  cors()(req, res, () => {
    if (req.method === 'POST' && req.url === '/message') {
      let body = '';
      req.on('data', (chunk) => {
        body += chunk.toString();
      });

      req.on('end', () => {
        console.log('Получено сообщение:', body);
        res.end('Сообщение получено');
      });
    } else {
      res.statusCode = 404;
      res.end('Страница не найдена');
    }
  });
});

const PORT = process.env.PORT || 3001;

server.listen(PORT, () => {
  console.log(`Сервер запущен на порту ${PORT}`);
});
