const express = require('express')
const app = express()
const port = process.env.PORT || 3000

const books = require('./books.json')["books"]
const books2 = books.filter(d => d.category == '어린이');
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

app.get('/all', (req, res) => {
    res.send(books)
})
app.get('/%EC%96%B4%EB%A6%B0%EC%9D%B4', (req, res) => {
    res.send(books2)
})
app.get('/%EC%B2%AD%EC%86%8C%EB%85%84', (req, res) => {
    res.send(books3)
})
app.get('/%EC%A2%8B%EC%9D%80%EB%B6%80%EB%AA%A8', (req, res) => {
    res.send(books4)
})
app.get('/%EC%86%8C%EC%84%A4+%EC%8B%9C+%ED%9D%AC%EA%B3%A1', (req, res) => {
    res.send(books5)
})
app.get('/%EC%97%90%EC%84%B8%EC%9D%B4', (req, res) => {
    res.send(books6)
})
app.get('/%EC%9D%B8%EB%AC%B8%ED%95%99', (req, res) => {
    res.send(books7)
})
app.get('/%EC%82%AC%ED%9A%8C%EA%B3%BC%ED%95%99', (req, res) => {
    res.send(books8)
})
app.get('/%EC%97%AD%EC%82%AC', (req, res) => {
    res.send(books9)
})
app.get('/%EA%B3%BC%ED%95%99', (req, res) => {
    res.send(books10)
})
app.get('/%EC%98%88%EC%88%A0+%EB%8C%80%EC%A4%91%EB%AC%B8%ED%99%94', (req, res) => {
    res.send(books11)
})
app.get('/%EC%A2%85%EA%B5%90+%EC%97%AD%ED%95%99', (req, res) => {
    res.send(books12)
})
app.get('/%EA%B2%BD%EC%A0%9C%EA%B2%BD%EC%98%81', (req, res) => {
    res.send(books13)
})
app.get('/%EC%9E%90%EA%B8%B0%EA%B3%84%EB%B0%9C', (req, res) => {
    res.send(books14)
})
app.get('/%EC%99%B8%EA%B5%AD%EC%96%B4', (req, res) => {
    res.send(books15)
})
app.get('/%EA%B0%80%EC%A0%95+%EC%9A%94%EB%A6%AC+%EB%B7%B0%ED%8B%B0', (req, res) => {
    res.send(books16)
})
app.get('/%EA%B1%B4%EA%B0%95+%EC%B7%A8%EB%AF%B8+%EB%A0%88%EC%A0%80', (req, res) => {
    res.send(books17)
})
app.get('/%EA%B8%B0%ED%83%80', (req, res) => {
    res.send(books18)
})

app.listen(port, () => {
    console.log(`App is listening to port ${port}`)
})
