# 2015, Day 9: All in a Single Night

Every year, Santa manages to deliver all of his presents in a single night.

## Part 1

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the _shortest distance_ he can travel to achieve this?

For example, given the following distances:

    London to Dublin = 464
    London to Belfast = 518
    Dublin to Belfast = 141
    

The possible routes are therefore:

    Dublin -> London -> Belfast = 982
    London -> Dublin -> Belfast = 605
    London -> Belfast -> Dublin = 659
    Dublin -> Belfast -> London = 659
    Belfast -> Dublin -> London = 605
    Belfast -> London -> Dublin = 982
    

The shortest of these is `London -> Dublin -> Belfast = 605`, and so the answer is `605` in this example.

What is the distance of the shortest route?

Your puzzle answer was `117`.

## Part 2

The next year, just to show off, Santa decides to take the route with the _longest distance_ instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be `982` via (for example) `Dublin -> London -> Belfast`.

What is the distance of the longest route?

Your puzzle answer was `909`.


## Solution Notes

A classical Travelling Salesman Problem, which is (fortunately!) easily solvable with brute force since there are only eight destinations.

* Part 1, Python: 186 bytes, ~100 ms
* Part 2, Python: 186 bytes, ~100 ms
