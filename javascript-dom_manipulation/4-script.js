document.getElementById('add_item').addEventListener('click', function () {
  const newItem = document.createElement('li'); // Create a new <li> element
  newItem.textContent = 'Item'; // Set the text of the new <li> element
  document.querySelector('.my_list').appendChild(newItem); // Add the new <li> to the <ul> with class 'my_list'
});
