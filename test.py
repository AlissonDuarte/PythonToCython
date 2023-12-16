import time
import example
import example_python

start_time = time.time()
perms = example.factorial(500000)
end_time = time.time()
print("Execution time:", end_time - start_time, "seconds")


import example_python
start_time = time.time()
example_python.factorial(500000)
end_time = time.time()

print("Execution time:", end_time - start_time, "seconds")