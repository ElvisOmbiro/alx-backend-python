#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon July  08 10:09:00 2024

@Author: Elvis Ombiro
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for max_delay seconds and returns a
    random number between 0 and max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
