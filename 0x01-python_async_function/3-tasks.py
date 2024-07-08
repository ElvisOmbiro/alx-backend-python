#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon July 10 10:13:00 2024

@Author: Elvis Ombiro
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Task to sleep for random seconds"""
    return asyncio.create_task(wait_random(max_delay))
