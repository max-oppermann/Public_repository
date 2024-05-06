The relevant entries are the directories CS50P, CS50x, Princeton Algorithms I, and the file Exercises-ISLP.ipynb.  

If you're a potential employer, you may be interested in my [Big Five traits](https://www.personalityassessor.com/ipip300/results=1535620-821/). You may also be interested in my *g*eneral cognitive ability yet lack the testing resources to infer it. The `explanation.md` in the `cognitive-metrics` directory could be interesting in that case.

# Exercises for ISLP

What it says on the tin; updated as I progress through the book. For more, see the notebook. The table of contents isn’t functional on GitHub; use https://nbviewer.org/ and paste the link to the notebook within my repository, i. e., https://github.com/max-oppermann/Public_repository/blob/master/Exercises-ISLP.ipynb, to have a functional  ToC (or just download the file and open it in JupyterLabs).

# Algorithms I

Weeks 1–5 of the Coursera Cours “Algorithms, Part I” by Robert Sedgewick entail exercises necessary to pass the course (at least 80% per exercise according to the autograder). Getting a certificate for passing the course costs money, so this is my proof I finished the course. The entire course is in Java, which I had never used before and would like to never use again (except for Part II, maybe). Luckily it is relatively similar to C, in my opinion.  
Week 1: Percolation. 100%. [specification](https://coursera.cs.princeton.edu/algs4/assignments/percolation/specification.php)  
Week 2: Deques and Randomized Queues. 98%. [specification](https://coursera.cs.princeton.edu/algs4/assignments/queues/specification.php)  
Week 3: Collinear Points. 95% (pretty hard!). [specification](https://coursera.cs.princeton.edu/algs4/assignments/collinear/specification.php)  
Week 4: 8 Puzzle. 97%. [specification](https://coursera.cs.princeton.edu/algs4/assignments/8puzzle/specification.php)   
Week 5: Kd-Trees. 85% (one of the functions does not actually solve the problem, but only gets very close). [specification](https://coursera.cs.princeton.edu/algs4/assignments/kdtree/specification.php)  

The “specifications” are the actual exercises and give an idea of the (considerable) complexity of these problems.

# CS50

CS50P is relatively unremarkable. The exercises can be found on the courses [website](https://cs50.harvard.edu/python/2022/) on the left within each week’s material.  

I did the 2024 version of [CS50x](https://cs50.harvard.edu/x/2024/). There are some interesting exercises: “tideman” in Pset3, all of Pset5, “fiftyville” in Pset7, and “finance” in Pset9:  
Tideman and Inheritance (Pset5) use recursive functions, making them substantially more complicated than the other exercises. Fiftyville is simply fun – although I probably didn’t do it as intended since I manually inferred the correct answer via several separate SQL queries.  
Finance is about creating a website where users can trade stocks with fictitious money and where all trades can be accessed in a history; the prices are actually real time prices for the stocks via requests from the web. It isn’t particularly complicated, but combines lots of Python code to interact with a server (via Flask) and a database and html templates. Lots of the code is actually written for you, which poses its own challenges of understanding ca. 100 lines of someone else’s code. On the other hand, it’s necessary to modify the database, work that is not apparent just from looking at it. For a detailed view of how much work is done by the student it’s probably easier to look at the original exercise and compare to my code.
