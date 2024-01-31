#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id.
// The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
// Only print users with completed tasks
// You must use the module request

const axios = require('axios');
const process = require('process');

const getCompletedTasks = async (apiUrl, userId) => {
    try {
        const response = await axios.get(apiUrl);
        const tasks = response.data;
        
        // Filtering the completed tasks
        const completedTasks = tasks.filter(task => task.userId === userId && task.completed);
        
        // Printing the number of completed tasks
        console.log(`${userId}: ${completedTasks.length}`);
    } catch (error) {
        console.error(`${error.message}`);
    }
};

if (process.argv.length === 4) { // Corrected the typo in 'length'
    const apiUrl = process.argv[2];
    const userId = parseInt(process.argv[3]);
    getCompletedTasks(apiUrl, userId);
}
