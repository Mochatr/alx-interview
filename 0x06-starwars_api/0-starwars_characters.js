#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  try {
    const data = JSON.parse(body);
    if (!data.characters || !Array.isArray(data.characters)) {
      console.error('Unexpected API response');
      return;
    }

    const characters = data.characters;
    characters.forEach((character) => {
      request(character, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error:', charError);
          return;
        }
        const charData = JSON.parse(charBody);
        console.log(charData.name);
      });
    });
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
