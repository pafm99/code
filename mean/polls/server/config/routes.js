const users = require('./../controllers/users.js');
const polls = require('./../controllers/polls.js');
const path = require('path');

module.exports = function (app) {
	//users
	app.post('/users', users.login);
	app.get('/users/one', users.getID);
	app.get('/users/logout', users.logout);

	//polls
	app.post('/polls', polls.create);
	app.get('/polls', polls.getPolls); //get all poll
	app.delete('/polls/:id', polls.delete);
	app.get('/options/:id', polls.getOptions); //get all optins
	app.get('/polls/:id', polls.getPoll); //get one poll
	app.put('/options', polls.vote);
	app.get('/options/one/:id', polls.getOption) //get one option
	app.all("*", (req, res, next) => {
		res.sendFile(path.resolve("./client/dist/index.html"));
	})
};