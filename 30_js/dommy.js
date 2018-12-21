// HEADING HERE

var listButton = document.getElementById('b');
var orderedList = document.getElementById('thelist');

listButton.addEventListener('click', function() {
    // create new list item
    let newListItem = document.createElement('li');
    newListItem.innerHTML = 'HELLO';

    // append new list item to ordered list
    orderedList.appendChild(newListItem);
    
}
                           );

var headingTag = document.getElementById('h');

// show list item on mouseover
orderedList.addEventListener('mouseover', function(e) {
    console.log(e);
    let itemText = e['path'][0]['innerHTML'];
    headingTag.innerHTML = itemText;
}
                            );

// revert heading to Hello World! if mouse outside <ol>
orderedList.addEventListener('mouseout', function() {
    headingTag.innerHTML = 'Hello World!';
}
                            );

// delete list item if pressed
orderedList.addEventListener('click', function(e) {
    let listItemElem = e['path'][0];
    listItemElem.remove();
}
                            );
