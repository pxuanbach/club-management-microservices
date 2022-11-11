require('dotenv').config();

const serviceUrlMap = JSON.parse(process.env.SERVICE_URL_MAP)
const urlStore = serviceUrlMap.map(url => {
    return url + "/events"
})

const eventTypeStore = {
    User: {
        Created: "users:created",
    },
    Club: {
        Created: "clubs:created",
    }
}

module.exports = { serviceUrlMap, urlStore, eventTypeStore };