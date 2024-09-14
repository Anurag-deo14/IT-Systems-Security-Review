const express = require('express');
const app = express();

app.use(express.json());

app.get('/', (req, res) => {
    res.send('Welcome to the Mock IT System');
});

// Simulate an admin login route with weak security
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    if (username === 'admin' && password === '1234') {
        res.status(200).send('Logged in as admin');
    } else {
        res.status(401).send('Unauthorized');
    }
});

app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
