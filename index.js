const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/login.html');
});

app.get('/api/data', (req, res) => {
  res.json({ message: 'Hello from the server!' });
});

app.post('/api/data', (req, res) => {
  console.log(req.body);
  res.json({ message: 'Data received!' });
});

app.listen(3000, () => {
  console.log('Server is running on port 3000.');
});