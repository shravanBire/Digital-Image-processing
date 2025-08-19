import cv2
import numpy as np
from collections import Counter

img = cv2.imread("gray_image.jpeg", cv2.IMREAD_GRAYSCALE)
pixels = img.flatten()

freq = Counter(pixels)
symbols = list(freq.keys())
prob = [f/sum(freq.values()) for f in freq.values()]

codes = {}

def shannon_fano(symbols, probs, code=""):
    if len(symbols) == 1:
        codes[symbols[0]] = code
        return
    
    total = sum(probs)
    acc = 0
    split = 0
    for i, p in enumerate(probs):
        acc += p
        if acc >= total/2:
            split = i+1
            break

    shannon_fano(symbols[:split], probs[:split], code+"0")
    shannon_fano(symbols[split:], probs[split:], code+"1")

sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
symbols, counts = zip(*sorted_items)
probs = [c/sum(counts) for c in counts]

shannon_fano(list(symbols), list(probs))

encoded_img = "".join([codes[p] for p in pixels])

print("Original size (bits):", len(pixels)*8)
print("Compressed size (bits):", len(encoded_img))
print("Compression Ratio:", round((len(pixels)*8)/len(encoded_img), 2))
