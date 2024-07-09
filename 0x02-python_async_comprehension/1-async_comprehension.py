#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue July 09 10:48:00 2024

@Author: Elvis Ombiro
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async comprehension"""
    numbers = [number async for number in async_generator()]
    return numbers
