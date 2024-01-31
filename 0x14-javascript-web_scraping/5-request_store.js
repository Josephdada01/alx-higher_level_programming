#!/usr/bin/node
// a script that gets the contents of a webpage and stores it in a file.
// The first argument is the URL to request
// The second argument the file path to store the body response
// The file must be UTF-8 encoded
// You must use the module request

const axios = require('axios');
const fs = require('fs');

const saveWebpageContent = async (url, filePath) => {
  try {
    const response = await axios.get(url);
    fs.writeFileSync(filePath, response.data, 'utf-8');
  } catch (error) {
    console.error(`${error.message}`);
  }
};

if (process.argv.length === 4) {
  const url = process.argv[2];
  const filePath = process.argv[3];
  saveWebpageContent(url, filePath);
}
