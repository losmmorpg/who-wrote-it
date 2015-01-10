Who-Wrote-It predicts the author of a book. It learns from examples, so by giving it samples of books, you can train it to recognize those books.

categories.txt contains the list of authors to train from. You must create a folder for each author in the list, and in there put text files of that author's work. Thus, shakespeare/ contains examples of Shakespeare writing, etc.

<b>To use the program, run bayes.py.</b> You input a filename with the work you want to classify. It will output its best prediction for the author of the book.

Example session:
<pre>
Enter name of file to be classified: test/london.txt

*** Predicted category: london ***</pre>

The program uses a Bayes classifier based on each author's unique style of word choice, so it can also be used to classify informal writing, spam, happy vs. sad messages, etc.
