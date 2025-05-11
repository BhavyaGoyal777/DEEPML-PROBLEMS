import numpy as np

def kl_divergence_normal(mu_1, sigma_1, mu_2, sigma_2):
    termOne = np.log(sigma_2/sigma_1)
	termTwo = ((sigma_1**2) + ((mu_1-mu_2)**2)) / (2*(sigma_2)**2)
    termThree = -0.5
    value = termOne + termTwo + termThree

    return value
