$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    $.each(data.results, function (index, results) {
      $('UL#list_movies').append($('<ul></ul>').text(results.title));
      console.log(results.title);
    });
  });
});
