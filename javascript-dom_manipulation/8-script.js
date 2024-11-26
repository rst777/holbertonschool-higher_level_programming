window.onload = function() {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())  // Convert the response to JSON
    .then(data => {
      document.getElementById('hello').textContent = data.hello; // Display the "hello" translation in the element
    })
    .catch(error => {
      console.error('Error fetching data:', error);  // Handle errors
    });
};
