Conditional Probability Calculator



Contributors:
- Sinchan Samajdar (Student ID: 02130429)
- Srinivas Prajwal Balakuntla Ravi Prakash (Student ID: 02101895)

Code Files
1. conditional probability calculator.py: Implements Bayesian network inference logic. Reads the joint distribution table and performs conditional probability calculations.
2. bonus.py: Python program to visualize Bayesian network.
3. bonus.png: Image of the graph generated in the bonus problem.

Files
- joint_distribution.py: Contains the joint distribution table in the form of a Python dictionary.
- bayesian_queries.py: Sample queries for Bayesian inference.
- output.txt: Generated file containing the results of the queries after inference.

Usage
The program is designed for Python 3.x.

To run:
1. Run 'conditional probability calculator.py'.
2. The output answers will be displayed to the command line.
3. Change the inputs as required in line 34, 35. 

Code Overview
conditional probability calculator.py:
The core logic works as follows:
- The joint distribution table is parsed into a Python dictionary.
- Queries are parsed into events and evidence.
- A Bayesian inference algorithm performs conditional probability calculations:
  - Probability is calculated using the provided joint distribution.
  - Results are written to the command line.
- The code is structured to be modular, with separate functions for each stage.

bonus.py:
- The Bayesian network is visualized using the networkx library.
- It uses a directed graph to represent the dependencies between nodes.
- The graph is exported as an image to bonus.png

Customizing
To use a different joint distribution or queries:
- Replace the contents of the lists 'event','evidence' in line 34 and 35 .
- Re-run 'conditional probability calculator.py' to perform inference on the new inputs.