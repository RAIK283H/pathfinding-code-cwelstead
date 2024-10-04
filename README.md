# Pathfinding Starter Code
### Random Path

This pathing algorithm works by choosing pseudo-random nodes that can legally be traveled to, and traveling to them until the target node has been hit and the end node has been reached. There are a few limitations placed on this algorithm to make it more efficient.
 - If the current node of the player has more than 1 node connected to it, do not travel to the node that was most recently visited.
 - If the length of the algorithm exceeds 2 times the length of the graph, start again from scratch at the first node.

The first limitation prevents the path from redunantly traveling between nodes back and forth, and makes linear graphs much more efficient to travel. The second limitation does a lot to prevent infinite loops, as well as allows the graph to be traversed in a reasonable amount of time.

### Average Distance per Node

The new statistic, Average Distance per Node (displayed as Avg. Dist per Node), is a representation of the average distance the player has to travel from one node to the next. This is calculated by taking the current distance that the player has traveled and dividing it by the total number of nodes the player will visit, a.k.a. the length of the path list.