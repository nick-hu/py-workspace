Quizzer 1.0 - Question making for teachers
==========================================

To make questions, compose a text file in the following format
and save it in the "data" directory. The filename of the text file
will be the "Quiz file" name, without the ".txt". (The format
must be followed precisely or else errors may occur!)

Line #
1	Write the question on this line.
2	Write the hint on this line.
3	Write the answer on this line (in lowercase).
4	Write the health cost and XP gain on this line, separated by a space
5	(Leave a blank line)
6	Write the next question on this line.
7	Write the next question's hint on this line.
etc.

At the end of the file, leave TWO blank lines.

Since the question will be inserted into HTML, you can use HTML
tags to style your question (e.g. you can use <br> for newlines).
However, note that pyFLTK only uses HTML2.

See the sample.txt file for an example of a test file.

Quizzer 1.0 - Option customization for teachers
===============================================

To customize quiz options, such as amount of heals, hints, cheats, and more,
simply run "quizconfig.py"

Some recommended themes:
------------------------

Format: Heal/Heal Amount/Hints/Cheats/Max. HP/Regeneration/Max. XP

--EASY--
Invincible: 0/0/3/1/100/0/1000 (Set no health cost for questions)
Healthy: 3/20/2/1/200/0.75/1000
Health Boost: 1/50/3/1/100/0.5/1000

--MEDIUM--
Classic: 1/10/3/1/100/0.25/1000
Deluxe: 2/20/6/2/200/0.25/2000

--HARD--
Hardcore: 0/0/0/0/100/0/1000
Wither: 0/0/0/0/100/-0.25/1000
Sudden Death: 0/0/0/0/1/0/1000

--OTHER--
No-XP: 1/10/3/1/100/0.25/0
Plain: 0/0/0/0/100/0/0 (Set no health cost for questions)