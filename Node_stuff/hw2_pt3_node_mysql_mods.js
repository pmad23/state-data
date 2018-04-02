// ALL ATTEMPTS AT GETTING PART 3 TO WORK -- NONE SUCCESSFUL


SELECT p.name, COUNT(f.friend) as count
FROM Person p, Friends f
WHERE p.login = f.login
GROUP BY p.name
ORDER BY count DESC


//======================================================================

var mysql = require('mysql');
var con = mysql.createConnection({
  host: "fling.seas.upenn.edu",
  user: "josepma",
  password: "Daisymae0)",
  database: "josepma"
});

con.connect(function(err) {
  if (err) throw err;
  con.query("SELECT p.name, COUNT(f.friend) as count FROM Person p, Friends f WHERE p.login = f.login GROUP BY p.name ORDER BY count DESC", function (err, result, fields) {
    if (err) throw err;
    console.log(fields);
    console.log(result);
  });
});

//========================================================================

app.get('/friendships', function(request, response) {
        response.sendFile(path.join(__dirname, '/', 'friendships.html'));
})

app.get('/script2.js', function(request, response) {
        response.sendFile(path.join(__dirname, '/', 'script2.js'));
})

//================================ index.js ============================

var mysql = require('mysql');
var con = mysql.createConnection({
  host: "fling.seas.upenn.edu",
  user: "josepma",
  password: "Daisymae0)",
  database: "josepma"
});
var obj = {};
app.get('/data', function(req, res){
    con.query('SELECT p.name, COUNT(f.friend) as count FROM Person p, Friends f WHERE p.login = f.login GROUP BY p.name ORDER BY count DESC', function (err, result) {
        if(err){
            throw err;
        } else {
            obj = {print: result};
            res.render('print', obj);
        }
    });
});

//===================================================
app.get('/data', function (req, res) {
    var mysql = require('mysql');
    var connection = mysql.createConnection({
  host: "fling.seas.upenn.edu",
  user: "josepma",
  password: "Daisymae0)",
  database: "josepma"
  });
    connection.connect((err, connection) => {
        if(err) { 
            res.send({ err }) 
        } else {
            var queryString = 'SELECT p.name, COUNT(f.friend) as count FROM Person p, Friends f WHERE p.login = f.login GROUP BY p.name ORDER BY count DESC';

            connection.query(queryString, (err, data) => {
                if(err) { 
                    res.send({ err }) 
                } else {
                    res.send({ data });
                }
            });
        }
    });
    connection.end();
});


// ========================================================================

app.get('getData', function (req, res) {
    var mysql = require('mysql');
    var connection = mysql.createConnection({ ... });
    connection.connect((err, connection) => {
        if(err) { 
            res.send({ err }) 
        } else {
            var queryString = 'SELECT * FROM ...';

            connection.query(queryString, (err, data) => {
                if(err) { 
                    res.send({ err }) 
                } else {
                    res.send({ data });
                }
            });
        }
    });
    connection.end();
});

//=====================================================

// code should display render.html when get request
app.get('/render', function(req, res){
    res.render(__dirname + '/render.html', function(req, res){


     });
});

//=========================================================

var app = angular.module('Friends',[]);
app.controller('friendsController', function($scope, $http) {
    $http.get('/getData').then(function(data) {
        $scope.friends = data;
    });
});
