var express = require('express')
var app = express()
var path = require('path');
var cors = require('cors')
app.use(cors())
app.set('port', (process.env.PORT || 5000))
app.use(express.static(__dirname + '/public'))

/* trying to set database specifications
var mysql = require('mysql');
var con = mysql.createConnection({
  host: "",
  user: "",
  password: "",
  database: ""
});
*/

/*
con.connect(function(err)){
if(!err) {
	console.log("Database connected..");
} else {
	console.log("Error connecting to database!");
}
});
*/

app.get('/', function(request, response) {
  response.send('Hello World!')
})

app.get('/test', function(request, response) {
  response.send('I am a test page, behold my might and glory!')
})

app.get('/costofliving', function(request, response) {
        response.sendFile(path.join(__dirname, '/', 'cost_of_living.html'));
})

app.get('/COL_script.js', function(request, response) {
        response.sendFile(path.join(__dirname, '/', 'COL_script.js'));
})

app.get('/styles.css', function(request, response) {
        response.sendFile(path.join(__dirname, '/', 'styles.css'));
})

/*
app.get('/bikes', function(request, response) {
	response.sendFile(path.join(__dirname, '/', 'bikes.html'));
})

app.get('/script.js', function(request, response) {
	response.sendFile(path.join(__dirname, '/', 'script.js'));
})
*/
app.listen(app.get('port'), function() {
  console.log("Node app is running at localhost:" + app.get('port'))
})


