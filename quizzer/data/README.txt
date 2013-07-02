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