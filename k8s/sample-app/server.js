const http = require('http');
const port = process.env.PORT || 8080;
const handler = (req, res) => {
  if (req.url === '/error') {
    // simulate error
    console.error("Simulated error!");
    res.writeHead(500, {'Content-Type': 'text/plain'});
    res.end('Simulated error\n');
    return;
  }
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello from sample-app\n');
};
const server = http.createServer(handler);
server.listen(port, () => console.log(`Server listening on ${port}`));

