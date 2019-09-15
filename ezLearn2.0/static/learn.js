var noteButton = document.querySelectorAll('.alt-nav-item')[0];
var learnButton = document.querySelectorAll('.alt-nav-item')[1];
var testButton = document.querySelectorAll('.alt-nav-item')[2];

var noteSection = document.querySelectorAll('section')[0];
var learnSection = document.querySelectorAll('section')[1];
var testSection = document.querySelectorAll('section')[2];

noteSection.style.display = 'block';

noteButton.style.color = '#fff';
noteButton.style.backgroundColor = '#38aecc';

noteSection.style.display = 'block';
learnSection.style.display = 'none';
testSection.style.display = 'none';


noteButton.addEventListener('click', function () {
    noteButton.style.color = '#fff';
    noteButton.style.backgroundColor = '#38aecc';
    learnButton.style.color = '#38aecc';
    learnButton.style.backgroundColor = 'transparent';
    testButton.style.color = '#38aecc';
    testButton.style.backgroundColor = 'transparent';

    noteSection.style.display = 'block';
    learnSection.style.display = 'none';
    testSection.style.display = 'none';
})

learnButton.addEventListener('click', function () {
    noteButton.style.color = '#38aecc';
    noteButton.style.backgroundColor = 'transparent';
    learnButton.style.color = '#fff';
    learnButton.style.backgroundColor = '#38aecc';
    testButton.style.color = '#38aecc';
    testButton.style.backgroundColor = 'transparent';

    noteSection.style.display = 'none';
    learnSection.style.display = 'block';
    testSection.style.display = 'none';
})

testButton.addEventListener('click', function () {
    noteButton.style.color = '#38aecc';
    noteButton.style.backgroundColor = 'transparent';
    learnButton.style.color = '#38aecc';
    learnButton.style.backgroundColor = 'transparent';
    testButton.style.color = '#fff';
    testButton.style.backgroundColor = '#38aecc';

    noteSection.style.display = 'none';
    learnSection.style.display = 'none';
    testSection.style.display = 'block';
})

//

var flashcards = document.querySelectorAll('.flashcard');

for (i = 0; i < flashcards.length; i++) {
    flashcards[i].addEventListener("click", function () {
        var answer = this.childNodes[3];
        if (answer.style.display === "block") {
            answer.style.display = "none";
        } else {
            answer.style.display = "block";
        }
    });
}
