**What is Nim?**

Nim game played with pebbles. Two players take turns picking from a pile of stones. Either picking 1 or 2 stones. Whoever picks the last stone wins.


**What are Grundy Numbers?**

Grundy Numbers are a way to analyse combination games. In other words, shows the optimal of stones to pick. 


**How are Grundy Numbers calculated?**

Grundy Numbers looks at all the pile sizes possible from your 1 or 2 stone pick. Calculates the 'grundy number' of each possible pile size (pile size % 3). If any of those 'grundy numbers' are 0, then it means the opponent gets a losing position next turn, making yours a winning position. By winning position, out of most situations left you win given the pile size.
