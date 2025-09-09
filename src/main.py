#!/usr/bin/env python3
import sys
import itertools

print("=== Word Combination Analyzer ===")

if len(sys.argv) < 2:
    print("Usage: python src/main.py word1 word2 ...")
    sys.exit(1)

words = sys.argv[1:]
print(f"Input words: {words}")

# Generate combinations
combinations = list(itertools.combinations(words, 2))
print(f"Found {len(combinations)} combinations:")

for i, combo in enumerate(combinations, 1):
    combined = ''.join(combo)
    print(f"{i}. {combo[0]} + {combo[1]} = {combined}")

# Generate permutations if more than 2 words
if len(words) > 2:
    permutations = list(itertools.permutations(words, 2))
    print(f"\nFound {len(permutations)} permutations:")
    for i, combo in enumerate(permutations, 1):
        combined = ''.join(combo)
        print(f"{i}. {combo[0]} + {combo[1]} = {combined}")
