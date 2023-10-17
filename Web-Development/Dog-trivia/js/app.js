$(document).ready(function () {
  /* -- questions -- */
  var questions = [
    {
      question: "Normal adult dogs have how many teeth?",
      choices: ["24", "38", "42", "32"],
      qNum: 0,
      correct: 2,
    },
    {
      question: "Through what part of the body do dogs sweat?",
      choices: ["Mouth", "Ears", "Nose", "Paws"],
      qNum: 1,
      correct: 3,
    },
    {
      question: "What is a dog’s most highly developed sense?",
      choices: ["Taste", "Smell", "Sight", "Touch"],
      qNum: 2,
      correct: 1,
    },
    {
      question: "What is the favorite dog breed of the Queen of England?",
      choices: ["Corgi", "Basenji", "Poodle", "Pomeranian"],
      qNum: 3,
      correct: 0,
    },
    {
      question: "Which dog breed is the smallest of them all?",
      choices: ["Dachshund", "Shih tzu", "Pomeranian", "Chihuahua"],
      qNum: 4,
      correct: 3,
    },
    {
      question: "Which dog breed has a black tongue?",
      choices: ["Husky", "Labrador", "Weimaraner", "Chow Chow"],
      qNum: 5,
      correct: 3,
    },
  ];

  //global variables
  var numberCorrect = 0;
  var currentQuestion = 0;

  $("#trivia").on("click", "#submit", function () {
    scoreUpdate();
    currentQuestion++;
    nextQuestion();
  });

  //reload
  $("#trivia").on("click", "#retry_button", function () {
    window.location.href = "";
  });

  function scoreUpdate() {
    var answer = $("input[type='radio']:checked").val();
    if (answer == questions[currentQuestion].correct) {
      numberCorrect++;
    }
    if (numberCorrect == 1) {
      $("#dog_image img").attr("src", "images/dog_eigth.jpg").fadeIn();
    } else if (numberCorrect == 2) {
      $("#dog_image img").attr("src", "images/dog_quarter.jpg").fadeIn();
    } else if (numberCorrect == 3) {
      $("#dog_image img").attr("src", "images/dog_half.jpg").fadeIn();
    } else if (numberCorrect == 4) {
      $("#dog_image img").attr("src", "images/dog_threequarter.jpg").fadeIn();
    } else if (numberCorrect == 5) {
      $("#dog_image img").attr("src", "images/dog_seventheigth.jpg").fadeIn();
    } else if (numberCorrect == 6) {
      $("#dog_image img").attr("src", "images/dog_complete.jpg").fadeIn();
    }
  }

  function nextQuestion() {
    if (currentQuestion < 6) {
      $(".question").remove();
      $("#answer_choices input").remove();
      $("#answer_choices span").remove();

      var newQuestion =
        '<div class="question">' +
        questions[currentQuestion].question +
        '</div><div id="answer_choices"><input type="radio" name="option" class="option" value="0"><span class="answer">' +
        questions[currentQuestion].choices[0] +
        '</span><br><input type="radio" name="option" class="option" value="1"><span class="answer">' +
        questions[currentQuestion].choices[1] +
        '</span><br><input type="radio" name="option" class="option" value="2"><span class="answer">' +
        questions[currentQuestion].choices[2] +
        '</span><br><input type="radio" name="option" class="option" value="3"><span class="answer">' +
        questions[currentQuestion].choices[3] +
        '</span><br></div><div id="button"><input type="button" id="submit" value="Submit Answer"><span id="hint"></span><input type="button" id="retry_button" value="Try Again!"></div>';
      $("#trivia").html(newQuestion);
    } else {
      $(".question").remove();
      $("#answer_choices input").remove();
      $("#answer_choices span").remove();
      $("#submit").css("display", "none");
      $("#retry_button").css("display", "inline");
      if (numberCorrect == 1) {
        var congrats =
          '<span id="final">Congratulations on finishing the quiz. You correctly answered ' +
          numberCorrect +
          " question. </span>";
        $("#answer_choices").css("margin-left", "275px");
        $("#answer_choices").html(congrats);
      } else {
        var congrats =
          '<span id="final">Congratulations on finishing the quiz. You correctly answered ' +
          numberCorrect +
          " questions. </span>";
        $("#answer_choices").css("margin-left", "275px");
        $("#answer_choices").html(congrats);
      }
    }
  }
});
