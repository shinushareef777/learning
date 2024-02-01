let mysql = require("mysql");
let config = require("./config");
let connection = mysql.createConnection(config);

let sql = `SELECT * FROM todos WHERE id=?`;

connection.query(sql,[3], (error, results, fields) => {
  if (error) {
    return console.error(error.message);
  }
  console.log(results);
})

connection.end();