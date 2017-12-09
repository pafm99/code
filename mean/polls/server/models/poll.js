const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const PollSchema = new mongoose.Schema({
	question: {
		type: String,
        minLength: [8, "Enter a question of at least 8 characters."],
		required: [true, "Enter a question. How are you going to have a poll with no question?"]
	},
    _options: [ {
        type: Schema.Types.ObjectId,
        ref: 'Option',
    } ],
    creator: {
        type: String,
        required: [true, "Please have a creator."]
    }
}, {timestamps: true})


const Poll = mongoose.model('Poll', PollSchema)