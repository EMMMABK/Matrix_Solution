
Gaussian Elimination and Matrix Inversion Tool

This Python program solves systems of linear equations using Gaussian elimination and finds the inverse of matrices. It includes an interactive menu to choose between solving equations and finding the inverse of a matrix.

Features:

	1.	Solve a system of linear equations using Gaussian elimination, with support for systems with infinite solutions.
	2.	Find the inverse of a square matrix, showing each step of the process.

Prerequisites

	•	Python 3.x
	•	NumPy (Install using pip install numpy)

Installation

	1.	Clone the repository or download the script:

git clone https://github.com/EMMMABK/matrix-tool.git

Or download the algebra_matrix_nd_way.py script directly.

	2.	Install NumPy if not already installed:

pip install numpy



Usage

	1.	Navigate to the folder containing the script:

cd matrix-tool


	2.	Run the script:

python algebra_matrix_nd_way.py


	3.	Select an option from the menu:
	•	Option 1: Solve a system of equations using Gaussian elimination.
	•	Option 2: Find the inverse of a matrix.
	4.	Input the matrix data when prompted. Enter each row as a space-separated line of numbers.

Example:

If the system asks for a matrix (e.g., 3x3), you can input:

1 2 3
4 5 6
7 8 9

For systems of equations, the program will solve using Gaussian elimination. For matrix inversion, it will output the steps and the inverse.

Exiting

To exit the program, choose Option 3 from the menu.

Note:

	•	For Gaussian elimination, you may input the value of a free variable (e.g., x2) when prompted for solutions with infinite possibilities.
	•	If the matrix is singular (non-invertible), the program will notify you.

