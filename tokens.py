#!/usr/bin/env python3

tokens = [str(((2**64 / 3) * i) - 2**63) for i in range(3)]
print(tokens)
