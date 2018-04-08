//Include express library for setting up web server
var express = require('express')
var app = express()
var cors = require('cors')

//Feature setup
app.use(cors())
app.set('port', (process.env.PORT || 13000))
app.use(express.static(__dirname + "/public"))

app.get("/", function(req, resp){
  resp.send("Landing page")
})

app.listen(app.get('port'), function(){
  console.log("Project is now up and running on port ", app.get('port'))
})
