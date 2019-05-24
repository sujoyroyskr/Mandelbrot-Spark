# Mandelbrot-Spark
Creating a Mandelbrot Set with Default and Load Balance Partitioning and comparing them with respect to Memory and Time.


# What is MandelBrot..?
It is a set of complex numbers, which has a highly convoluted fractel broundry.
In this, the function [f(z) = z^2 + c], does not diverge when iterated from z = 0 i.e for which the sequence f(0), f(f(0)), etc. remains bounded in the absolute value. (Source - Wikipedia)

Here I'll be using the computation of the Madelbrot set to explore how partitioning aﬀects load balancing in Spark. The code for computing the Mandelbrot at a position (x,y) is:

# Code for Mandelbrot
def mandelbrot(x, y):
    z = c = complex(x, y)
    iteration = 0 
    max_iteration = 511 # This is the arbitrary cutoff 
    while abs(z) < 2 and iteration < max_iteration: 
        z = z * z + c 
        iteration += 1 
    return iteration
    
An issue with parallelizing this computation is that the mandelbrot function can require anywhere from 0 to 511 iterations to return. In addition, as we can see in the image and will encounter below, locations close to one another tend to have similar ﬁnal iteration counts.

Load Balancing: In parallel computation with multiple subtasks, it is usually best for each task to be approximately equal in execution time. Slow tasks are known as “stragglers”, and can cause the computation to have poor parallelism (particularly if badly scheduled). When you try to come up with an improved partitioning strategy, you should aim to have each partition/task take roughly the same amount of time.

# Implementing the Mandalbrot Set

Implemented the computation of the Mandelbrot set, in the P2.py ﬁle provided above, with some helper functions, one for plotting the result (draw image), and another for exploring how much computation was done in each partition (sum values for partitions).

The following constraints were used: 
  • Compute an image of 2000×2000 pixels. 
  • For the pixel at (i,j), use x = (j/500.0)−2 and y = (i/500.0)−2. 
  • Divide the computation where you call mandelbrot into 100 partitions. 
  • Use the default partitioning strategy (i.e., do not use partitionBy().

Used the sum values for partitions, to produce a histogram of compute “eﬀort” on each partition. 
(plt.hist() and plt.savefig() have been used for this part.)

# Implementation Of Default Partitioning

In case of default partitioning, pixels have been divided evenly using the formula mentioned above and accordingly the result was calculated and histogram was generated.

# Implementation of Load Balanced Partitiong

In this the data was shuffled randomly after loading it into RDD, and accordingly the result was calculated and histogram was generated.

# Result

In case of Default Partitiong, it takes larger amount of memory and takes around 30-35 minutes to completey process itself.
While, In case of Load Balancing, it comparitively takes less memory and time from default partitioning. Load Balancing taked around 2-4 minutes to completely process itself.
