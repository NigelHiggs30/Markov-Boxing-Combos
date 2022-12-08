# Markov-Boxing-Combos

The code in this repository simulates and generates random sequences of punches used in a boxing match. It does this by first calculating the probability distribution of the length of the sequences of punches in the data. It then creates a bin to count the occurrences of each punch in the data, and uses this to calculate the probability distribution of each punch. The code then creates a Markov matrix, which is a square matrix that shows the probabilities of transitioning from one punch to another. The code then uses this Markov matrix to generate a random sequence of punches that matches the length distribution of the original data.

##Usage
To use this code, run the combo_generator() function, passing in the result of the punch_bin_counts() function and the original data as arguments. This will generate and print a random sequence of punches.

##Dependencies
This code requires the following Python packages:

'''
itertools
collections
'''

##Example
Here is an example of how to use this code to generate a random sequence of punches:

