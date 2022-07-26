const express = require('express')
const app = express()
const books = require('./books.json')["books"]

const port = process.env.PORT || 3000

const books3 = books.filter(d => d.category == '청소년');
const books4 = books.filter(d => d.category == '좋은부모');
const books5 = books.filter(d => d.category == '소설+시+희곡');
const books6 = books.filter(d => d.category == '에세이');
const books7 = books.filter(d => d.category == '인문학');
const books8 = books.filter(d => d.category == '사회과학');
const books9 = books.filter(d => d.category == '역사');
const books10 = books.filter(d => d.category == '과학');
const books11 = books.filter(d => d.category == '예술+대중문화');
const books12 = books.filter(d => d.category == '종교+역학');
const books13 = books.filter(d => d.category == '경제경영');
const books14 = books.filter(d => d.category == '자기계발');
const books15 = books.filter(d => d.category == '외국어');
const books16 = books.filter(d => d.category == '가정+요리+뷰티');
const books17 = books.filter(d => d.category == '건강+취미+레저');
const books18 = books.filter(d => d.category != '어린이' && d.category != '청소년' && d.category != '좋은부모' && d.category != '소설+시+희곡' && d.category != '에세이' && d.category != '인문학' && d.category != '사회과학' && d.category != '역사' && d.category != '과학' && d.category != '예술+대중문화' && d.category != '종교+역학' && d.category != '경제경영' && d.category != '자기계발' && d.category != '외국어' && d.category != '가정+요리+뷰티' && d.category != '건강+취미+레저');

app.get('/', (req, res) => {
    res.send(books)
})
app.get('/어린이', (req, res) => {
    const books2 = books.filter(d => d.category == '어린이');
    res.send(books2)
})
app.get('/청소년', (req, res) => {
    res.send(books3)
})
app.get('/좋은부모', (req, res) => {
    res.send(books4)
})
app.get('/소설+시+희곡', (req, res) => {
    res.send(books5)
})
app.get('/에세이', (req, res) => {
    res.send(books6)
})
app.get('/인문학', (req, res) => {
    res.send(books7)
})
app.get('/사회과학', (req, res) => {
    res.send(books8)
})
app.get('/역사', (req, res) => {
    res.send(books9)
})
app.get('/과학', (req, res) => {
    res.send(books10)
})
app.get('/예술+대중문화', (req, res) => {
    res.send(books11)
})
app.get('/종교+역학', (req, res) => {
    res.send(books12)
})
app.get('/경제경영', (req, res) => {
    res.send(books13)
})
app.get('/자기계발', (req, res) => {
    res.send(books14)
})
app.get('/외국어', (req, res) => {
    res.send(books15)
})
app.get('/가정+요리+뷰티', (req, res) => {
    res.send(books16)
})
app.get('/건강+취미+레저', (req, res) => {
    res.send(books17)
})
app.get('/기타', (req, res) => {
    res.send(books18)
})

app.listen(port, () => {
    console.log(`App is listening to port ${port}`)
})
