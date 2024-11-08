Programs of varying length and complexity without overarching theme.

#### `matching_cards.py`
Simulates the matching cards problem: Shuffle a deck of $N$ cards, labeled 1 through $N$. What is the probability that at least one card in position $i$ has $i$ written on it (turning over the seventh card and it has a 7 on it, e. g., but also drawing 1, 2, 3, 4, ...)?  
Solving this analytically gives $1-\frac1e\approx0.63$, which is in fact what the program converges to for simulating the problem often enough. "Often enough" turns out to be at least 10,000 times. I also plot the convergence behavior from 10 to 10,000 replications.  

#### `monty_hall.py`  
Simulates the classic Monty Hall problem, allowing you to play multiple rounds. The car is randomly placed behind one of three doors, you are asked to choose one. After your choice, Monty reveals a non-car door, and you are given the option to switch. The program tracks your wins and losses, and also compares your results with theoretical probabilities of winning by always staying or always switching (simulates 1000 rounds of always staying/switching). The simulation continues until you decide to stop.