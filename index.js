//Include express library for setting up web server
var express = require('express')
var app = express()
var cors = require('cors');
var path = require('path')
var std_path = 'Node_stuff'

//Feature setup
app.use(cors())
app.set('port', (process.env.PORT || 13000))
app.use(express.static(__dirname + "/public"))

//Index page
app.get("/", function(req, resp){
  resp.send("Landing page")
})

app.get('/costofliving', function(request, response) {
        response.sendFile(path.join(__dirname, '/', std_path, 'cost_of_living.html'));
})

app.get('/COL_script.js', function(request, response) {
        response.sendFile(path.join(__dirname, '/', std_path, 'COL_script.js'));
})

app.get('/styles.css', function(request, response) {
        response.sendFile(path.join(__dirname, '/', std_path, 'styles.css'));
})

app.listen(app.get('port'), function(){
  console.log("Project is now up and running on port ", app.get('port'))
})
