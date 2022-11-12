require('dotenv').config();

const serviceUrlMap = [
    process.env.USERS_SERVICE_URL,
    process.env.CLUBS_SERVICE_URL,
]

const eventTypeStore = {
    User: {
        Created: "users:created",
    },
    Club: {
        Created: "clubs:created",
    }
}

module.exports = { serviceUrlMap, eventTypeStore };