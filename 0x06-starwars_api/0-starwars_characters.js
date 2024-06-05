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
    const characterPromises = characters.map((character) => {
      return new Promise((resolve, reject) => {
        request(character, (charError, charResponse, charBody) => {
          if (charError) {
            reject(charError);
            return;
          }
          const charData = JSON.parse(charBody);
          resolve(charData.name);
        });
      });
    });

    Promise.all(characterPromises)
      .then((names) => {
        names.forEach((name) => {
          console.log(name);
        });
      })
      .catch((err) => {
        console.error('Error:', err);
      });
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
