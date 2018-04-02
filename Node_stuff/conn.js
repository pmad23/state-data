var mysql = require('mysql');
var con = mysql.createConnection({
  host: "",
  user: "",
  password: "",
  database: ""
});

con.connect(function(err) {
  if (err) throw err;
  con.query("SELECT p.name, COUNT(f.friend) as count FROM Person p, Friends f WHERE p.login = f.login GROUP BY p.name ORDER BY count DESC", function (err, result, fields) {
    if (err) throw err;
    console.log(fields);
    console.log(result);
  });
});
