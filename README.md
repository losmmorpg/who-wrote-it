# Author

Predicts the author of a book. It learns from examples, so by giving it samples of books, you can train it to recognize those books.

## How to Use
To use the program, run bayes.py. It'll prompt you to input a filename with the work you want to classify. Then, it'll output its best prediction for the author of the book.

categories.txt contains the list of authors to train from. You must create a folder for each author in the list, and in there put text files of that author's work. Thus, shakespeare/ contains examples of Shakespeare writing, etc.

Example session:

    Enter name of file to be classified: test/london.txt
    
    *** Predicted category: london ***

The program uses a Bayes classifier based on each author's unique style of word choice, so it can also be used to classify informal writing, happy vs. sad messages, etc.
