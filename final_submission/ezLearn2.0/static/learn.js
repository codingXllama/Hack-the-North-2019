var noteButton = document.querySelectorAll('.alt-nav-item')[0];
var learnButton = document.querySelectorAll('.alt-nav-item')[1];
var testButton = document.querySelectorAll('.alt-nav-item')[2];

var noteSection = document.querySelectorAll('section')[0];
var learnSection = document.querySelectorAll('section')[1];
var testSection = document.querySelectorAll('section')[2];

noteSection.style.display = 'block';

noteButton.style.color = '#fff';
noteButton.style.backgroundColor = '#38aecc';

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

//quiz
(function () {
    function buildQuiz() {
        // we'll need a place to store the HTML output
        const output = [];

        // for each question...
        myQuestions.forEach((currentQuestion, questionNumber) => {
            // we'll want to store the list of answer choices
            const answers = [];

            // and for each available answer...
            for (letter in currentQuestion.answers) {
                // ...add an HTML radio button
                answers.push(
                    `<label>
              <input type="radio" name="question${questionNumber}" value="${letter}">
              ${letter} :
              ${currentQuestion.answers[letter]}
            </label>`
                );
            }

            // add this question and its answers to the output
            output.push(
                `<div class="question"> ${currentQuestion.question} </div>
          <div class="answers"> ${answers.join("")} </div>`
            );
        });

        // finally combine our output list into one string of HTML and put it on the page
        quizContainer.innerHTML = output.join("");
    }

    function showResults() {
        // gather answer containers from our quiz
        const answerContainers = quizContainer.querySelectorAll(".answers");

        // keep track of user's answers
        let numCorrect = 0;

        // for each question...
        myQuestions.forEach((currentQuestion, questionNumber) => {
            // find selected answer
            const answerContainer = answerContainers[questionNumber];
            const selector = `input[name=question${questionNumber}]:checked`;
            const userAnswer = (answerContainer.querySelector(selector) || {}).value;

            // if answer is correct
            if (userAnswer === currentQuestion.correctAnswer) {
                // add to the number of correct answers
                numCorrect++;

                // color the answers green
                answerContainers[questionNumber].style.color = "lightgreen";
            } else {
                // if answer is wrong or blank
                // color the answers red
                answerContainers[questionNumber].style.color = "red";
            }
        });

        // show number of correct answers out of total
        resultsContainer.innerHTML = `${numCorrect} out of ${myQuestions.length}`;
    }

    const quizContainer = document.getElementById("quiz");
    const resultsContainer = document.getElementById("results");
    const submitButton = document.getElementById("submit");
    const myQuestions = [
        {
            question: "Who is the strongest?",
            answers: {
                a: "Superman",
                b: "The Terminator",
                c: "Waluigi, obviously"
            },
            correctAnswer: "c"
        },
        {
            question: "What is the best site ever created?",
            answers: {
                a: "SitePoint",
                b: "Simple Steps Code",
                c: "Trick question; they're both the best"
            },
            correctAnswer: "c"
        },
        {
            question: "Where is Waldo really?",
            answers: {
                a: "Antarctica",
                b: "Exploring the Pacific Ocean",
                c: "Sitting in a tree",
                d: "Minding his own business, so stop asking"
            },
            correctAnswer: "d"
        }
    ];

    // display quiz right away
    buildQuiz();

    // on submit, show results
    submitButton.addEventListener("click", showResults);
})();