# Python standard libraries
import argparse
import sys
# Extra libraries
import tensorflow as tf

FLAGS = None

def conquer(_):
    # TODO Conquer the universe

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main=conquer, argv=[sys.argv[0]] + unparsed)