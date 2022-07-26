const express = require('express')
const app = express()
const books = require('./book.json')

const port = process.env.PORT || 3000

app.get('/', (req, res) => {
    res.send("Manchester United Players")
})

app.get('/books', (req, res) => {
    res.send(books)
})

app.listen(port, () => {
    console.log(`App is listening to port ${port}`)
})