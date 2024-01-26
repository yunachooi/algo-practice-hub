from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
card = deque(range(1, n + 1))

while 1 < len(card):
  card.popleft()
  card.rotate(-1)
    
print(card[0])
