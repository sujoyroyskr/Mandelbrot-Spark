import os

import sys

spark_home = os.environ.get('SPARK_HOME', None)

if not spark_home:
    raise ValueError('SPARK_HOME environment variable is not set')

sys.path.insert(0, os.path.join(spark_home, 'python'))
sys.path.insert(0, os.path.join(spark_home, 'C:/spark-2.3.0-bin-hadoop2.7/python/lib/py4j-0.10.6-src.zip')) ## may need to adjust on your system depending on which Spark version you're using and where you installed it.
filename=os.path.join(spark_home, 'python/pyspark/shell.py')
exec(compile(open(filename, "rb").read(), filename, 'exec'))

from P2 import *

import pyspark
#sc = pyspark.SparkContext()
para_sc = sc.parallelize(range(2000), 10)
cart = para_sc.cartesian(para_sc)
rdd = cart.map(lambda s: [s, mandelbrot((s[0]/500.0 - 2), (s[1]/500.0 - 2))])
draw_image(rdd)

rdd1 = sum_values_for_partitions(rdd)

plt.hist(rdd1.collect())
plt.savefig('P2a_hist.png')
