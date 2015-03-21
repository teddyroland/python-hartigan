PYTHON-HARTIGAN is a python script that provides an unsupervised method to determine an optimal value K in K-Means clustering. The script is an implementation of Hartigan's Rule -- essentially it measures the change in goodness-of-fit as the number of clusters increases. This implementation is based on Chiang & Mirkin (2009), §3.1(B). Feel free to change the script in any way; it is commented to guide any edits you may need to make.

If you want to build your intuition regarding the values that come out of Hartigan's Rule, I suggest setting 'threshold' parameter to 0 or an arbitrarily small value and including a line in the while-loop that will print 'H_Rule' after each iteration. I also highly recommend looking over Chiang & Mirkin's article which notes some of the limitiations on Hartigan's Rule.

PYTHON-HARTIGAN relies on two standard scientific Python packages: numpy & scikit-learn.

A similar function in R is FitKMeans() in the 'useful' package, which also implements Hartigan's Rule.


Chiang & Mirkin (2009): http://www.dcs.bbk.ac.uk/~mirkin/papers/00357_07-216RR_mirkin.pdf
