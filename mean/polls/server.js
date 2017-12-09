const express = require('express');
const app = express();
const bp = require('body-parser');
const path = require('path')
const session = require('express-session');
const port = 8000;

app.use(session({secret:'SecretWord', resave: false,saveUninitialized: true}))
app.use(bp.json())
app.use(express.static(path.join(__dirname, 'client', 'dist')))

require('./server/config/mongoose.js')

var routes_setter = require('./server/config/routes.js');
routes_setter(app);

app.listen(port, function(){
    console.log('Running on port ' + port);
})