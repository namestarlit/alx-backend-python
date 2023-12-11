#!/usr/bin/env python3
"""using type annotations with asyncio"""
import asyncio
from sys import argv


async def countdown(tag: str, count: int) -> None:
    while (count > 0):
        print(f"T-minus {count} ({tag})")
        await asyncio.sleep(0.1)
        count -= 1
    print("Blastoff!")


if __name__ == "__main__":
    tag = argv[1]
    count = int(argv[2])

    asyncio.run(countdown(tag, count))
