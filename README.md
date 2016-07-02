# Problem's describtion
![Problem's describtion](https://gitlab.com/mahdavipanah/EscapeGraph/raw/e09755d9daafe3df744f58ebe4a5dcdac1c9d1e4/describtion.jpg)

# Problem's assumptions
1. Every escape path sould have it's unique set of vertices.
2. If two escape paths have shared vertices, only one of them is accepted as escape path.
3. If two escape paths have shared vertices, The one which has been seen sooner, will be accepted.
4. Order of seeing the paths relate to order of seeing the start points.
5. Order of seeing the start points is the exact order of them in input.txt

# Input rules
The input grid graph informations should be placed in input.txt
* The first line of input.txt is grid's size: n (grid has n <sup>2</sup> nodes)
* The n next lines are informations about nodes:
	* Every node has 4 directions that can have one of these values:
		* 0: If that direction is not connected.
		* 1: If that direction is connected.
		* 3: If that direction has no more nodes (the node is on border)

    	Order of directions are like this: Left-Right-Up-Down

        Example of a node's information: 3130
 * Next lines (to an empty line) are starting points, each line contains a starting point.

There is an example test case in input.txt. You can read it to see how input.txt should be filled.

# Prerequisites
* Python2 (python 2.7 is tested)