#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer.
// The first argument is the movie ID
// You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
// You must use the module request

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`${error.message}`);
    process.exit(1);
  }

  if (response.statusCode === 200) {
    const filmsData = JSON.parse(body).results;

    // Filter films where Wedge Antilles is present
    const filmsWithWedgeAntilles = filmsData.filter((film) =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );

    console.log(`${filmsWithWedgeAntilles.length}`);
  }
});
