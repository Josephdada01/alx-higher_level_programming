// avaScript script that fetches the character name from this URL:
// https://swapi-api.alx-tools.com/api/people/5/?format=json
// The name must be displayed in the HTML tag DIV#character
$(document).ready(function () {
  // fetches the character name from the url
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    const characterName = data.name;
    $('DIV#character').text(characterName);
  })
    .fail(function (error) {
      console.error(error);
    });
});
