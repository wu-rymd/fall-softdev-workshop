// Peter Cwalina, Raymond Wu (team PCRW)
// SoftDev1 pd7
// K30 -- Sequential Progression III: Season of the Witch
// 2018-12-21

// PHASE III

var orderedList = document.getElementById('thelist');
var listButton = document.getElementById('b');

listButton.addEventListener('click', function() {
    // create new list item
    let newListItem = document.createElement('li');
    newListItem.innerHTML = 'HELLO';

    // append new list item to ordered list
    orderedList.appendChild(newListItem);
}
                           );

var headingElem = document.getElementById('h');

// show list item on mouseover
orderedList.addEventListener('mouseover', function(e) {
    // console.log(e);
    let itemText = e['path'][0]['innerHTML'];
    headingElem.innerHTML = itemText;
}
                            );

// revert heading to Hello World! if mouse outside <ol>
orderedList.addEventListener('mouseout', function() {
    headingElem.innerHTML = 'Hello World!';
}
                            );

// delete list item if pressed
orderedList.addEventListener('click', function(e) {
    let listItemElem = e['path'][0];
    listItemElem.remove();
}
                            );

// PHASE IV

var fibList = document.getElementById('fiblist');
var fibButton = document.getElementById('fb');

var fibArray = [0, 0, 1];
fibButton.addEventListener('click', function() {
    fibArray[0] = fibArray[1];
    fibArray[1] = fibArray[2];
    fibArray[2] = fibArray[0] + fibArray[1];

    // create new list item
    let newFibItem = document.createElement('li');
    newFibItem.innerHTML = fibArray[1];
    
    // append new list item to ordered list
    fibList.appendChild(newFibItem);
}
                          );

