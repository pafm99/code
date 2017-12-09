const mongoose = require('mongoose');
const User = mongoose.model('User');

module.exports = {
    login(req, res) {
        User.findOne({name: req.body.name}, (err, user) => {
			if(err){
				return res.status(404).json(err)
			}
			else if(user){
				req.session.user = user
				res.json({user: user})
			}
			else{
				let user = new User(req.body);
				user.save((err) => {
					if(err){
						return res.status(404).json(err);
					}
					else{
						console.log(`saved ${user}`)
						req.session.user = user;
						res.json({user: user});
					}
				})
			}
		})
    },

    getID(req, res) {
		if(req.session.user){
			return res.json(req.session.user);
		}
		else{
			return res.status(500).json("Not logged in")
		}
	},

    logout(req, res) {
        req.session.destroy()
		return res.json('logged out');
    }
}