$(document).ready(function() {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        method: 'GET',
        success: function(data) {
            let movies = data.results;
            for (let i = 0; i < movies.length; i++) {
                $('#list_movies').append('<li>' + movies[i].title + '</li>');
            }
        },
        error: function(error) {
            console.error('Error fetching data:', error);
        }
    });
});
