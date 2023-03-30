const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const messageSchema = new Schema({
    userId: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'User',
        required: true
    },
    content: {
        type: String,
        required: true
    },
    to: {
        type: String
    },
    socketID: {
        type: String
    },
    from: Object,
    createdAt: {
        type: Date,
        default: Date.now
    }
});

const Message = mongoose.model('Message ', messageSchema);
exports.Message = Message;