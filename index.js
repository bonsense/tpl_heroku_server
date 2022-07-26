const express = require('express')
var cors = require('cors')
const app = express()
app.use(cors())
//Without Cors no access...

const port = process.env.PORT || 3000

const books = require('./books.json')["books"]
const children = books.filter(d => d.category == '어린이');
const youngadult = books.filter(d => d.category == '청소년');
const parenting = books.filter(d => d.category == '좋은부모');
const novelpoetryplay = books.filter(d => d.category == '소설+시+희곡');
const essay = books.filter(d => d.category == '에세이');
const humanities = books.filter(d => d.category == '인문학');
const sociology = books.filter(d => d.category == '사회과학');
const history = books.filter(d => d.category == '역사');
const science = books.filter(d => d.category == '과학');
const artculture = books.filter(d => d.category == '예술+대중문화');
const religion = books.filter(d => d.category == '종교+역학');
const economy = books.filter(d => d.category == '경제경영');
const selfhelp = books.filter(d => d.category == '자기계발');
const foreignlanguage = books.filter(d => d.category == '외국어');
const homecookbeauty = books.filter(d => d.category == '가정+요리+뷰티');
const healthleisure = books.filter(d => d.category == '건강+취미+레저');
const etc = books.filter(d => d.category != '어린이' && d.category != '청소년' && d.category != '좋은부모' && d.category != '소설+시+희곡' && d.category != '에세이' && d.category != '인문학' && d.category != '사회과학' && d.category != '역사' && d.category != '과학' && d.category != '예술+대중문화' && d.category != '종교+역학' && d.category != '경제경영' && d.category != '자기계발' && d.category != '외국어' && d.category != '가정+요리+뷰티' && d.category != '건강+취미+레저');

app.get('/all', (req, res) => {
    res.send(books)
})
app.get('/children', (req, res) => {
    res.send(children)
})
app.get('/youngadult', (req, res) => {
    res.send(youngadult)
})
app.get('/parenting', (req, res) => {
    res.send(parenting)
})
app.get('/novelpoetryplay', (req, res) => {
    res.send(novelpoetryplay)
})
app.get('/essay', (req, res) => {
    res.send(essay)
})
app.get('/humanities', (req, res) => {
    res.send(humanities)
})
app.get('/sociology', (req, res) => {
    res.send(sociology)
})
app.get('/history', (req, res) => {
    res.send(history)
})
app.get('/science', (req, res) => {
    res.send(science)
})
app.get('/artculture', (req, res) => {
    res.send(artculture)
})
app.get('/religion', (req, res) => {
    res.send(religion)
})
app.get('/economy', (req, res) => {
    res.send(economy)
})
app.get('/selfhelp', (req, res) => {
    res.send(selfhelp)
})
app.get('/foreignlanguage', (req, res) => {
    res.send(foreignlanguage)
})
app.get('/homecookbeauty', (req, res) => {
    res.send(homecookbeauty)
})
app.get('/healthleisure', (req, res) => {
    res.send(healthleisure)
})
app.get('/etc', (req, res) => {
    res.send(etc)
})

app.listen(port, () => {
    console.log(`App is listening to port ${port}`)
})
