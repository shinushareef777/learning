let mysql = require("mysql");
let config = require("./config");
let connection = mysql.createConnection(config);

// let sql = `
//             INSERT INTO todos(title, completed) VALUES ('Learn how to insert new value', true)
//           `;
let stmt = `
  INSERT INTO todos(title, completed) VALUES ?
`;
let inserts = [
  ['Insert multiple rows at a time', false],
  ['It should work properly', true]
]


connection.query(stmt, [inserts], (err, results, fields) => {
  if (err) {
    return console.error(error.message);
  }
  console.log('Rows affected: ', results.affectedRows);
});

connection.end();
