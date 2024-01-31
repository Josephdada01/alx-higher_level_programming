#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id.
// The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
// Only print users with completed tasks
// You must use the module request

const axios = require('axios');
const process = require('process');

const getCompletedTasks = async (apiUrl) => {
  try {
    const response = await axios.get(apiUrl);
    const tasks = response.data;

    const taskCompleted = {};

    tasks.forEach(task => {
      if (task.completed === true) {
        const userId = task.userId;
        taskCompleted[userId] = (taskCompleted[userId] || 0) + 1;
      }
    });

    console.log(taskCompleted);
  } catch (error) {
    console.error(`${error.message}`);
  }
};

if (process.argv.length === 3) {
  const apiUrl = process.argv[2];
  getCompletedTasks(apiUrl);
}
