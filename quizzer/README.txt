Quizzer 1.0
===========


Setup:
------
Make sure you have the following:
    - Python 2.7
    - pyFLTK package


Gameplay:
---------
Run "quiz.py". A window should appear.

Enter the name of the quiz file for the quiz you are taking
in the box labelled "Quiz file"
(if you do not know what this is, ask your teacher).
If your teacher wishes to monitor your progress, enter the IP
address specified by the teacher in the box "Teacher IP".

Press "Start/Restart Quiz" to begin. If you specified an IP,
the text in that box should change to "Connected to teacher" to
indicate a succesful connection.

Questions will now be displayed in the viewer. Type out your
answer in the "Answer:" box and click "Submit" to submit your answer.
Note that your answer is case-insensitive, but everything else matters
(e.g. "hello" is the same as "HELLO" but 6.00 is not the same as 6). 

Observe the status box below the answer input box to see
the results of your answer (correct/incorrect).

At the end of the quiz, your score will be displayed.
Press "Start/Restart" to redo the current quiz or to do another quiz.


Effects:
--------
The HP bar displays how much health you have left. If you run out of
health (and you are unable to heal yourself), you lose!
Each question, if answered correctly, will regenerate some health,
and if answered incorrectly will reduce your health.

The XP bar displays your experience. The amount of experience for
each question is different.

The progress bar displays your progress through the quiz (% complete).

The "Heal" button, when clicked, will regenerate 10HP.
The "Hint" button will display a hint in the status box.
The "Cheat" button will place the correct answer in the answer box.
The amount of uses remaining of each ability is displayed on its button.