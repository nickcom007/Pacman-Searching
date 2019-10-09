# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # Get starting position and initial
    start_state = problem.getStartState()
    initial = (start_state,[],0)
    # Create a fringe and a visited set
    fringe = util.Stack()
    visited = set()
    # Push the start state with cost to the fringe.
    fringe.push(initial)
    visited.add(start_state)
    # while the fringe is not empty
    while not fringe.isEmpty():
        current = fringe.pop()
        state = current[0]
        route = current[1]

        # If pop out then visited
        visited.add(state)

        # If is goal, then return route
        if problem.isGoalState(state):
            return route

        # Find all successor of current
        # Will return a list of tuples (successor_state, action, stepCost)
        successors = problem.getSuccessors(state)
        for neighbour in successors:
            # if haven't visited
            if neighbour[0] not in visited:
                # update state
                # convert tuple to list
                temp = list(current)
                temp[0] = neighbour[0]
                temp[1] = current[1].copy()
                temp[1] += [neighbour[1]]
                temp[2] += 1
                # push all neighbours
                next = tuple(temp)
                fringe.push(next)




    ##util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # initialize the start state
    start_state = problem.getStartState()
    initial = (start_state,[],0)
    # Create a fringe(Queue) and a visited set
    fringe = util.Queue()
    visited = set()
    # Push the start state with cost to the fringe.
    fringe.push(initial)
    # while fringe is not empty
    while not fringe.isEmpty():
        # Current is first element added
        current = fringe.pop()
        state = current[0]
        route = current[1]
        # then visted
        visited.add(state)
        # If is goal, then return route
        if problem.isGoalState(state):
            return route

        # Will return a list of tuples (successor_state, action, stepCost)
        successors = problem.getSuccessors(state)

        for neighbour in successors:
            # if haven't visited
            # Add all unvisited neighbours to the fringe
            if neighbour[0] not in visited:
                # update state
                # convert tuple to list
                temp = list(current)
                temp[0] = neighbour[0]
                temp[1] = current[1].copy()
                temp[1] += [neighbour[1]]
                temp[2] += 1
                # convert back to tuple
                next = tuple(temp)
                # push back
                fringe.push(next)
                # set as visited
                visited.add(neighbour[0])


    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Get starting position and initial
    start_state = problem.getStartState()
    initial = (start_state, [], 0)
    # Create a fringe and a visited set
    fringe = util.PriorityQueue()
    visited = set()
    # Push the start state with cost to the fringe.
    cost = problem.getCostOfActions(initial[1])
    fringe.push(initial,priority=cost)
    # while the fringe is not empty
    while not fringe.isEmpty():
        current = fringe.pop()
        state = current[0]
        route = current[1]

        # If is goal, then return route
        if problem.isGoalState(state):
            return route

        visited.add(state)
        # Find all successor of current
        # Will return a list of tuples (successor_state, action, stepCost)
        successors = problem.getSuccessors(state)
        for neighbour in successors:
            # if haven't visited
            if neighbour[0] not in visited:
                # update state
                # convert tuple to list
                temp = list(current)
                temp[0] = neighbour[0]
                temp[1] = current[1].copy()
                temp[1] += [neighbour[1]]
                temp[2] += 1

                # push all neighbours into queue
                next = tuple(temp)
                cost = problem.getCostOfActions(next[1])
                fringe.push(next,priority=cost)
                # If goal, do not set visited
                if problem.isGoalState(next[0]):
                    continue
                # else visited once pushed
                else:
                    visited.add(neighbour[0])

    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # Get starting position and initial
    start_state = problem.getStartState()
    initial = (start_state, [], 0)
    # Create a fringe and a visited set
    fringe = util.PriorityQueue()
    visited = set()
    # Push the start state with cost to the fringe.
    cost = problem.getCostOfActions(initial[1])
    # calculate heuristic value
    heuristic_value = heuristic(start_state,problem)
    # combine cost and heuristic value as priority
    combined_cost = cost + heuristic_value
    fringe.push(initial, priority=combined_cost)
    # while the fringe is not empty
    while not fringe.isEmpty():
        current = fringe.pop()
        state = current[0]
        route = current[1]

        # If is goal, then return route
        if problem.isGoalState(state):
            return route

        visited.add(state)
        # Find all successor of current
        # Will return a list of tuples (successor_state, action, stepCost)
        successors = problem.getSuccessors(state)
        for neighbour in successors:
            # if haven't visited
            if neighbour[0] not in visited:
                # update state
                # convert tuple to list
                temp = list(current)
                temp[0] = neighbour[0]
                temp[1] = current[1].copy()
                temp[1] += [neighbour[1]]
                temp[2] += 1

                # push all neighbours into queue
                next = tuple(temp)
                cost = problem.getCostOfActions(next[1])
                # calculate heuristic value
                heuristic_value = heuristic(next[0], problem)
                # combine cost and heuristic value as priority
                combined_cost = cost + heuristic_value
                fringe.push(next, priority=combined_cost)
                # If goal, do not set visited
                if problem.isGoalState(next[0]):
                    continue
                # else visited once pushed
                else:
                    visited.add(neighbour[0])

    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
