const mongoose = require('mongoose');
const Poll = mongoose.model('Poll');
const Option = mongoose.model('Option')

module.exports = {

    getPolls(req, res) {
        Poll.find({}, (err, polls) => {
            if(err){
                return res.status(404).json(err);
            }
            return res.json(polls);
        })
    },

    create(req, res) {
        let newPoll = new Poll(
            {
                question: req.body.question, 
                creator: req.body.creator
            });
        newPoll.save((err) => {
            if(err){
                console.log("The poll was not saved.")
                return res.status(500).json(err);
            }
        });
        let newOptionOne = new Option(
            {
                option: req.body.optionone, 
                likes: 0
            });
        newOptionOne._poll = newPoll._id;
        newOptionOne.save((err) => {
            if(err){
                return res.status(404).json(err);
            }
        });
        let newOptionTwo = new Option(
            {
                option: req.body.optiontwo, 
                likes: 0
            });
        newOptionTwo._poll = newPoll._id;
        newOptionTwo.save((err) => {
            if(err){
                return res.status(404).json(err);
            }
        });

        let newOptionThree = new Option(
            {
                option: req.body.optionthree, 
                likes: 0
            });
        newOptionThree._poll = newPoll._id;
        newOptionThree.save((err) => {
            if(err){
                return res.status(404).json(err);
            }
        });
        let newOptionFour = new Option(
            {
                option: req.body.optionfour, 
                likes: 0
            });
        newOptionFour._poll = newPoll._id;
        newOptionFour.save((err) => {
            if(err){
                return res.status(404).json(err);
            }
        });
        return res.json("All clear!")
    },

    delete(req, res) {
        Poll.remove({_id: req.params.id}, (err) => {
            if(err) {
                return res.status(500).json(err);
            }
        })
        return res.json("Deleted!")
    },

    getOptions(req, res) {
        Option.find({_poll: req.params.id}, (err, options) => {
            if(err) {
                return res.status(404).json(err);
            }
            return res.json(options);
        })
    },

    getPoll(req, res) {
        Poll.findOne({_id: req.params.id}, (err, poll) => {
            if(err) {
                return res.status(404).json(err);
            }
            return res.json(poll);
        })
    },

    vote(req, res) {
        Option.update({_id: req.body._id},{$inc: {likes: 1}}, (err) => {
            if(err){
                return res.status(404).json(err);
            }
            return res.json("voted")
        })
    },

    getOption(req, res) {
        Option.findOne({_id: req.params.id}, (err, option) => {
            if(err){
                return res.status(404).json(err);
            }
            return res.json(option)
        })
    }

}