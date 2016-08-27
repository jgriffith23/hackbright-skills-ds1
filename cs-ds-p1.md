# Data Structures Skills Assessment Part 1

The following sections are my answers to the discussion questions for this 
assignment.

## Runtime

1. The total number of crackers in your box of animal crackers determines the 
workload of figuring out whether there's an elephant in the box. in the worst case,
you might look at every cracker in the box and still not find an elephant!

2. In ascending order by efficiency, the list of runtimes given should look like
this: O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n)

## Stacks and Queues

1a. The process of loading and unloading pallets onto a flatbed truck would be like a stack. The first pallet loaded would be the last pallet unloaded.
1b. Putting bottle caps on bottles of beer as they roll down an assembly line would be
like a queue. The first bottle on the line would be the first bottle to get a cap.
1c. Calculating the solution to the expression: 
2 + (7 * 4) - (3 / 2) would be a good place to use a stack. Here's how that might work:

```
push(2)
push(+)
push(()

--I just pushed an open paren! Eval expression until I see a closing paren.--

	push(7)
	push(*)
	push(4)
    
--I found a close paren! Eval substack.--
	pop(4)
    pop(*)
    
    --Operator!--
    pop(7)
    eval(7 * 4) => 28

pop(()
push(28)
push(-)
push(()

--I just pushed an open paren! Eval expression until I see a closing paren.--

	push(3)
	push(/)
	push(2)
    
--I found a close paren! Eval substack--
	pop(2)
    pop(/)
    
    --Operator!--
    pop(3)
    eval(3/2) => 1.5

pop(()
push(1.5)

--No more sub-expressions to evaluate. Stack contains: [2, + , 28, -, 1.5]--

pop(1.5)
pop(-)

--Operator!--

pop(28)
eval(28-1.5) => 26.5
pop(+)

--That's an operator!--

pop(2)
eval(2 + 26.5) => 28.5
```
*(Note: This is not a general use algorithm, as it doesn't account for the EMD part of PEMDAS.)*

2 . A queue would also be an appropriate data structure for a printer job list or a food delivery service (clients get put in the queue when they make orders and get dequeued as their orders are finished and sent out for delivery).

3 . A stack would also be an appropriate data structure for any application that wants to show information in reverse chronological order. For instance, your Twitter feed shows you the most recent tweet first and the oldest tweet last. A (perhaps naive) implementation of that feed might push tweets onto a stack as they happen over five minutes. After 5 minutes, a block of tweets would get rendered, with the most recent tweet at the top. (Though if you think about placing tweets on the bottom of the rendered block first, this could be a queue instead...and that might be better.)

Another place you could use a stack is in maze traversal. Start at an opening. Move forward 1 (push forward 1), turn left (push left), go forward 1 (push forward 1), and run into a wall. Go backward 1(pop forward 1), turn right (pop left), go back 1(pop forward 1) to get back where you started. Now, go forward 1 (push fwd 1), turn right (push right)...and so on.

## Linked Lists

1. The nodes are the boxes not labeled LLIST. The data in the first node is "Apple,"
the data in the second node is "Berry," and the data in the third node is "Cherry."

The head is the node referenced by LLIST.head, which is currently the node containing
the data "Apple." (An arrow points from LLIST.head to the node containing "Apple.")

The tail is the node containing "Cherry," because its next property references None. 
(But we're not currently tracking the tail.)

2. In a doubly-linked list, each node contains references to both the node before it 
 the node after it. In a singly-linked list, each node only contains a reference to
 the node after it.

3. Appending to a linked list is faster if we keep track of the tail because then, we don't have to start at the head and look at every node until we find one whose .next
property is None. We can just grab the tail, update its next reference to point at
the new node, and point the new node's next reference to None.

## Trees

1. In. a breadth first search, you'd visit the following nodes to get to burrito:

Food, Italian, Indian, Mexican, lasagna, pizza, tikka masala, saag, burrito 

(This is assuming an algorithm that always checks the left-most unchecked node
available.)

2. A depth first search algorithm would visit nodes in the following order to reach
Chicago-style:

food, Italian, lasagna, pizza, thin crust, Chicago-style

(This is assuming an algorithm that always checks the left-most unchecked node 
available.)

3. A binary search tree is designed for fast searching, so it has a "physical"
constraint a standard tree doesn't have. A binary tree's nodes can have only 0, 1,
or 2 children. 

In a binary search tree, the hierarchical organization of the data matters
less than organizing the data in a way that lets you throw away as many incorrect
results as possible when you search for a particular data point. One common 
organization technique is to add data to your tree such that all left children are
"less" than the parent and all right children are "greater" than the parent. Then,
all descendants to the left of the parent are less than all descendants on the right.