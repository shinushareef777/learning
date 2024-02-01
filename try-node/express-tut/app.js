const express = require("express");

const app = express();



app.get('/about', (req, res) => {
  res.status(200).send('about page')}); 

app.all("*", (req, res) => {
  res.status(404).send("Resource not found")
})

app.listen(2000, ()=> {
  console.log("Listening to port 2000")
})