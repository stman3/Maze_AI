# INTRODUCTION
___________________________________________________________________________________________________________________________________________________________
Pathfinding in computer games have been of research for many years, it can be considered the most popular Artificial Intelligence problem in the gaming industry.
In famous computer games a variant of this problem can be found, and it must be solved in real- time, and a path must be found.
Pathfinding simply answers the question “How can I get from here to there?”, usually the path from a starting point to a goal have several solutions.



<img width="536" alt="Screen Shot 1444-04-06 at 3 04 12 AM" src="https://user-images.githubusercontent.com/75269916/198908534-33d33b16-5122-41c8-95b6-7475fbbc288b.png">
                                              Figure.1 Maze

In the above figure is an example of a maze with some obstacles, if there is a solution it needs to
cover the following steps:
I. The path from the starting point “S” marked in green to the goal “G” marked in red.
II. How to move around obstacles.
III. How to find the shortest path (if the algorithm can do it).
IV. How to find it quickly.
some pathfinding algorithms cannot solve a problem like Figure.1, and some algorithms solve any pathfinding problems.
the topic of our report includes the following:
I. Two algorithms that can be used to solve the maze in Figure.1.
II. A sample program in python for the discussed algorithms.
III. Sample output for the discussed algorithms.


A* Search Algorithm
___________________________________________________________________________________________________________________________________________________________
A* is an informed searching algorithm meaning it uses information called heuristic to solve the problem, this algorithm is used to find the shortest path from a starting point to a goal.
This algorithm always searches for shorter paths first, which makes the algorithm optimal because it will find the solution with the least cost, and complete because it will find all the possible outcomes for the problem.

<img width="578" alt="Screen Shot 1444-04-06 at 3 08 29 AM" src="https://user-images.githubusercontent.com/75269916/198908694-98bee840-c1b1-4278-b883-2f80011a626c.png">
Figure.2 Weighted graph including heuristic

What makes this algorithm so potent is the use of weighted graphs Figure.2. A weighted graph is a graph that uses numbers to show the cost of taking each path, which means that the algorithm can take the path with the minimum cost and find the best or shortest route in terms of distance and time.
A major downside for this algorithm is that it takes a large amount of space to store every possible solution and a lot of time to find them.
___________________________________________________________________________________________________________________________________________________________
Implementation

The following graph is considered in the implementation:

<img width="833" alt="Screen Shot 1444-04-06 at 3 10 24 AM" src="https://user-images.githubusercontent.com/75269916/198908774-02a55610-8802-4d18-9997-00019dc3f3c9.png">
Figure.3 Maze Graph

The path taken by A* algorithm is as follows:

<img width="837" alt="Screen Shot 1444-04-06 at 3 10 35 AM" src="https://user-images.githubusercontent.com/75269916/198908795-b6834884-905b-4f01-b00a-35aa9ad493df.png">
Figure.4 A* Path

if you want to make it faster just change this line:

<img width="468" alt="Screen Shot 1444-04-06 at 3 12 47 AM" src="https://user-images.githubusercontent.com/75269916/198908854-bbadaed3-c0fc-4136-af52-67ff6c1f75fc.png">


