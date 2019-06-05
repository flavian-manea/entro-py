Pyschultz Python library for Entropy and Mutual Information using various estimators:

General remarks:

	- It works for Python 3+
	- API Matlab engine for python should be installed: https://uk.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html
	- It depends on numpy package and possibly matplotlib 
	- CDMentropy should be downloaded
https://pillowlab.princeton.edu/code_CDMentropy.html
	- The working directory of CDMentropy should be 
specified in the cdm.py script for both entries 

How it works:

	- A binary 3D matrix is passed [stimuli x word_length x timewindow]:2D matrix generates per stimulus
	-input arguments: -3D matrix X
			  -s: number of stimuli (default 1)
			  -dt: time bin (default 1)
	-entropy_all(X,s,dt): generates an entropy vector with values of entropy at each trial (time_window/time_bin) considering all stimuli
	-entropy(X, s, dt): generates a set of entropy vectors with values of entropy at each trial given each stimulus
	-mutual_information (X, s, dt): generates the mutual_information vector with values of inforamtion at each trial 