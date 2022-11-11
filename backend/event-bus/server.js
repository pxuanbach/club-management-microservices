const express = require('express');
const bodyParser = require('body-parser');
const axiosInstance = require('./axiosConfig');
var cors = require('cors');

const { urlStore, serviceUrlMap } = require('./store');
const httpLogger = require('./httpLogger');
const logger = require('./logger')

const corsOptions = {
    origin: serviceUrlMap,
    credentials: true,
    optionsSuccessStatus: 200,
};
PORT = 8005
const app = express();
app.use(cors(corsOptions))
app.use(bodyParser.json());
app.use(httpLogger);

app.post("/events", async (req, res) => {
    const event = req.body;
    // console.log(req)

    urlStore.map(url => {
        axiosInstance.post(url, event)
        logger.info(`POST ${url}`)
    })
    res.send({ detail: "OK" });
})

app.listen(PORT, () => {
    logger.info(`Server listening on port ${PORT}`);
});