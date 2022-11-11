const axiosInstance = require('axios');
const logger = require('./logger');

// Add a response interceptor
axiosInstance.interceptors.response.use(function (response) {
    // Any status code that lie within the range of 2xx cause this function to trigger
    return response;
}, function (error) {
    // Any status codes that falls outside the range of 2xx cause this function to trigger
    return error;
});

module.exports = axiosInstance