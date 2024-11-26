fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())  // Convert the response to JSON
  .then(data => {
    document.getElementById('character').textContent = data.name; // Display the character name
  })
  .catch(error => {
    console.error('Error fetching data:', error);  // Handle any errors
  });
