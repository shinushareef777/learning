const http = require('http')
const server = http.createServer((req, res) => {
  res.write("Hello from mars rover");
  res.end()
});

server.listen(5000)