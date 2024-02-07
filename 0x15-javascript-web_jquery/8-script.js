// JavaScript script that fetches and lists the title for all
// movies by using this URL:
// https://swapi-api.alx-tools.com/api/films/?format=json
// All movie titles must be list in the HTML tag UL#list_movies
// You can’t use document.querySelector to select the HTML tag
// You must use the JQuery API
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const titles = data.results;
    const $listTitles = $('UL#list_movies');

    titles.forEach(title => {
      const $li = $('<li>').text(title.title);
      $listTitles.append($li);
    });
  })
    .fail(function (error) {
      console.error(error);
    });
});
