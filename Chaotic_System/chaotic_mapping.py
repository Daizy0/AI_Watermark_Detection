import numpy as np

def chaotic_map(size):
    x = 0.5
    y = 0.5
    chaotic_sequence = []
    
    for _ in range(size):
        x = 3.9 * x * (1 - x)  
        y = 3.9 * y * (1 - y)  
        chaotic_sequence.append((x + y) % 1)  
        
    return chaotic_sequence

