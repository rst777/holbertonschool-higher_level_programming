fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())  // Convert the response to JSON
  .then(data => {
    const moviesList = document.getElementById('list_movies'); // Get the <ul> element
    data.results.forEach(movie => {
      const listItem = document.createElement('li');  // Create a new <li> for each movie
      listItem.textContent = movie.title;  // Set the title of the movie as the text content
      moviesList.appendChild(listItem);  // Append the <li> to the <ul>
    });
  })
  .catch(error => {
    console.error('Error fetching movies:', error);  // Handle errors
  });
