import time
import threading
import multiprocessing
import asyncio

# PRIME CHECK FUNCTION
def is_prime(n):
    
    #Check whether a number is prime.

    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# ASYNCIO IMPLEMENTATION
async def async_prime_finder(start, duration):
    #Asynchronously find the highest prime within the given time duration.
    end_time = time.time() + duration
    num = start
    last_prime = 0

    while time.time() < end_time:
        if is_prime(num):
            last_prime = num
        num += 1
        await asyncio.sleep(0)  # Yield control to allow async context switching

    return last_prime

async def run_async():
    print("[ASYNC] Searching...")
    start_time = time.time() 
    highest_prime = await async_prime_finder(0, 180)  # 3-minute limit(180 seconds)
    duration = time.time() - start_time # Calculate elapsed time
    print(f"[ASYNC] Highest prime found: {highest_prime} in {duration:.2f} seconds\n") 

# THREADING IMPLEMENTATION

def threaded_prime_worker(start, duration, result_container): 
    end_time = time.time() + duration 
    num = start
    last_prime = 0

    while time.time() < end_time:
        if is_prime(num):
            last_prime = num
        num += 1

    result_container.append(last_prime)

def run_threaded():
    
    #Run threaded prime search in a single thread and display the result.
    print("[THREADING] Searching...")
    result_container = []
    thread = threading.Thread(target=threaded_prime_worker, args=(0, 180, result_container))

    start_time = time.time()
    thread.start()
    thread.join()
    duration = time.time() - start_time

    print(f"[THREADING] Highest prime found: {result_container[0]} in {duration:.2f} seconds\n")

# MULTIPROCESSING IMPLEMENTATION

def mp_prime_worker(start, duration, return_dict):
    #Multiprocessing worker that finds highest prime in time limit.
    end_time = time.time() + duration
    num = start
    last_prime = 0

    while time.time() < end_time:
        if is_prime(num):
            last_prime = num
        num += 1

    return_dict['prime'] = last_prime

def run_multiprocessing():
    
    #Run multiprocessing version of the prime search and display result.

    print("[MULTIPROCESSING] Searching...")
    manager = multiprocessing.Manager()
    return_dict = manager.dict()

    start_time = time.time()
    process = multiprocessing.Process(target=mp_prime_worker, args=(0, 180, return_dict))

    process.start()
    process.join()
    duration = time.time() - start_time

    print(f"[MULTIPROCESSING] Highest prime found: {return_dict['prime']} in {duration:.2f} seconds\n")

# MAIN FUNCTION

if __name__ == '__main__':
    print("\n============================================")
    print("  Getting Prime Number(3 minutes each)")
    print("   Comparing: Async, Threading, Multiprocessing")
    print("============================================\n")

    # Run async
    asyncio.run(run_async())

    # Run threading
    run_threaded()

    # Run multiprocessing
    run_multiprocessing()
