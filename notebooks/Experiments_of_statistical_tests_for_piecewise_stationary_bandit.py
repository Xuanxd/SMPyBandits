
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Requirements-and-helper-functions" data-toc-modified-id="Requirements-and-helper-functions-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Requirements and helper functions</a></div><div class="lev2 toc-item"><a href="#Requirements" data-toc-modified-id="Requirements-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Requirements</a></div><div class="lev2 toc-item"><a href="#Mathematical-notations-for-stationary-problems" data-toc-modified-id="Mathematical-notations-for-stationary-problems-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Mathematical notations for stationary problems</a></div><div class="lev2 toc-item"><a href="#Generating-stationary-data" data-toc-modified-id="Generating-stationary-data-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Generating stationary data</a></div><div class="lev2 toc-item"><a href="#Mathematical-notations-for-piecewise-stationary-problems" data-toc-modified-id="Mathematical-notations-for-piecewise-stationary-problems-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Mathematical notations for piecewise stationary problems</a></div><div class="lev2 toc-item"><a href="#Generating-fake-piecewise-stationary-data" data-toc-modified-id="Generating-fake-piecewise-stationary-data-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Generating fake piecewise stationary data</a></div><div class="lev1 toc-item"><a href="#Python-implementations-of-some-statistical-tests" data-toc-modified-id="Python-implementations-of-some-statistical-tests-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Python implementations of some statistical tests</a></div><div class="lev2 toc-item"><a href="#A-stupid-detection-test-(pure-random!)" data-toc-modified-id="A-stupid-detection-test-(pure-random!)-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>A stupid detection test (pure random!)</a></div><div class="lev2 toc-item"><a href="#Monitored" data-toc-modified-id="Monitored-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Monitored</a></div><div class="lev2 toc-item"><a href="#CUSUM" data-toc-modified-id="CUSUM-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>CUSUM</a></div><div class="lev2 toc-item"><a href="#PHT" data-toc-modified-id="PHT-24"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>PHT</a></div><div class="lev2 toc-item"><a href="#Gaussian-GLR" data-toc-modified-id="Gaussian-GLR-25"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Gaussian GLR</a></div><div class="lev2 toc-item"><a href="#Bernoulli-GLR" data-toc-modified-id="Bernoulli-GLR-26"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Bernoulli GLR</a></div><div class="lev2 toc-item"><a href="#List-of-all-Python-algorithms" data-toc-modified-id="List-of-all-Python-algorithms-27"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>List of all Python algorithms</a></div><div class="lev1 toc-item"><a href="#Numba-implementations-of-some-statistical-tests" data-toc-modified-id="Numba-implementations-of-some-statistical-tests-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Numba implementations of some statistical tests</a></div><div class="lev2 toc-item"><a href="#Some-results" data-toc-modified-id="Some-results-31"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Some results</a></div><div class="lev1 toc-item"><a href="#Cython-implementations-of-some-statistical-tests" data-toc-modified-id="Cython-implementations-of-some-statistical-tests-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Cython implementations of some statistical tests</a></div><div class="lev2 toc-item"><a href="#Speeding-up-just-the-kl-functions" data-toc-modified-id="Speeding-up-just-the-kl-functions-41"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Speeding up just the <code>kl</code> functions</a></div><div class="lev2 toc-item"><a href="#Speeding-up-the-whole-test-functions" data-toc-modified-id="Speeding-up-the-whole-test-functions-42"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Speeding up the whole test functions</a></div><div class="lev3 toc-item"><a href="#PHT-in-Cython" data-toc-modified-id="PHT-in-Cython-421"><span class="toc-item-num">4.2.1&nbsp;&nbsp;</span>PHT in Cython</a></div><div class="lev3 toc-item"><a href="#Gaussian-GLR-in-Cython" data-toc-modified-id="Gaussian-GLR-in-Cython-422"><span class="toc-item-num">4.2.2&nbsp;&nbsp;</span>Gaussian GLR in Cython</a></div><div class="lev3 toc-item"><a href="#Bernoulli-GLR-in-Cython" data-toc-modified-id="Bernoulli-GLR-in-Cython-423"><span class="toc-item-num">4.2.3&nbsp;&nbsp;</span>Bernoulli GLR in Cython</a></div><div class="lev3 toc-item"><a href="#Some-results" data-toc-modified-id="Some-results-424"><span class="toc-item-num">4.2.4&nbsp;&nbsp;</span>Some results</a></div><div class="lev3 toc-item"><a href="#3-more-algorithms-implemented-in-Cython" data-toc-modified-id="3-more-algorithms-implemented-in-Cython-425"><span class="toc-item-num">4.2.5&nbsp;&nbsp;</span>3 more algorithms implemented in Cython</a></div><div class="lev1 toc-item"><a href="#Comparing-the-different-implementations" data-toc-modified-id="Comparing-the-different-implementations-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Comparing the different implementations</a></div><div class="lev2 toc-item"><a href="#Generating-some-toy-data" data-toc-modified-id="Generating-some-toy-data-51"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Generating some toy data</a></div><div class="lev2 toc-item"><a href="#Checking-time-efficiency" data-toc-modified-id="Checking-time-efficiency-52"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Checking time efficiency</a></div><div class="lev2 toc-item"><a href="#Checking-detection-delay" data-toc-modified-id="Checking-detection-delay-53"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Checking detection delay</a></div><div class="lev2 toc-item"><a href="#Checking-false-alarm-probabilities" data-toc-modified-id="Checking-false-alarm-probabilities-54"><span class="toc-item-num">5.4&nbsp;&nbsp;</span>Checking false alarm probabilities</a></div><div class="lev2 toc-item"><a href="#Checking-missed-detection-probabilities" data-toc-modified-id="Checking-missed-detection-probabilities-55"><span class="toc-item-num">5.5&nbsp;&nbsp;</span>Checking missed detection probabilities</a></div><div class="lev1 toc-item"><a href="#More-simulations-and-some-plots" data-toc-modified-id="More-simulations-and-some-plots-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>More simulations and some plots</a></div><div class="lev2 toc-item"><a href="#Run-a-check-for-a-grid-of-values" data-toc-modified-id="Run-a-check-for-a-grid-of-values-61"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>Run a check for a grid of values</a></div><div class="lev2 toc-item"><a href="#A-version-using-joblib.Parallel-to-use-multi-core-computations" data-toc-modified-id="A-version-using-joblib.Parallel-to-use-multi-core-computations-62"><span class="toc-item-num">6.2&nbsp;&nbsp;</span>A version using <code>joblib.Parallel</code> to use multi-core computations</a></div><div class="lev2 toc-item"><a href="#Checking-on-a-small-grid-of-values" data-toc-modified-id="Checking-on-a-small-grid-of-values-63"><span class="toc-item-num">6.3&nbsp;&nbsp;</span>Checking on a small grid of values</a></div><div class="lev2 toc-item"><a href="#Plotting-the-result-as-a-2D-image" data-toc-modified-id="Plotting-the-result-as-a-2D-image-64"><span class="toc-item-num">6.4&nbsp;&nbsp;</span>Plotting the result as a 2D image</a></div><div class="lev3 toc-item"><a href="#First-example,-for-Monitored" data-toc-modified-id="First-example,-for-Monitored-641"><span class="toc-item-num">6.4.1&nbsp;&nbsp;</span>First example, for <code>Monitored</code></a></div><div class="lev3 toc-item"><a href="#For-CUSUM" data-toc-modified-id="For-CUSUM-642"><span class="toc-item-num">6.4.2&nbsp;&nbsp;</span>For <code>CUSUM</code></a></div><div class="lev3 toc-item"><a href="#Second-example" data-toc-modified-id="Second-example-643"><span class="toc-item-num">6.4.3&nbsp;&nbsp;</span>Second example</a></div><div class="lev3 toc-item"><a href="#More-examples" data-toc-modified-id="More-examples-644"><span class="toc-item-num">6.4.4&nbsp;&nbsp;</span>More examples</a></div><div class="lev1 toc-item"><a href="#Conclusions" data-toc-modified-id="Conclusions-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Conclusions</a></div>

# # Requirements and helper functions

# ## Requirements
# 
# This notebook requires to have [`numpy`](https://www.numpy.org/) and [`matplotlib`](https://matplotlib.org/) installed.
# I'm also exploring usage of [`numba`](https://numba.pydata.org) and [`cython`](https://cython.readthedocs.io/en/latest/) later, so they are also needed.
# One function needs a function from [`scipy.special`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.comb.html#scipy.special.comb), and I use [`tqdm`](https://github.com/tqdm/tqdm#usage) for pretty progress bars for loops.
# [`joblib`](https://joblib.readthedocs.io/en/latest/) is used to have parallel computations (at the end).

# In[2]:


get_ipython().system('pip install watermark numpy scipy matplotlib numba cython tqdm joblib')
get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -m -p numpy,scipy,matplotlib,numba,cython,tqdm,joblib -a "Lilian Besson"')


# In[3]:


import numpy as np
import matplotlib.pyplot as plt
import numba


# In[4]:


def in_notebook():
    """Check if the code is running inside a Jupyter notebook or not. Cf. http://stackoverflow.com/a/39662359/.

    >>> in_notebook()
    False
    """
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':  # Jupyter notebook or qtconsole?
            return True
        elif shell == 'TerminalInteractiveShell':  # Terminal running IPython?
            return False
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter


# In[5]:


if in_notebook():
    from tqdm import tqdm_notebook as tqdm
    print("Info: Using the Jupyter notebook version of the tqdm() decorator, tqdm_notebook() ...")  # DEBUG
else:
    from tqdm import tqdm


# ## Mathematical notations for stationary problems
# 
# We consider $K \geq 1$ arms, which are distributions $\nu_k$.
# We focus on Bernoulli distributions, which are characterized by their means, $\nu_k = \mathcal{B}(\mu_k)$ for $\mu_k\in[0,1]$.
# A stationary bandit problem is defined here by the vector $[\mu_1,\dots,\mu_K]$.
# 
# For a fixed problem and a *horizon* $T\in\mathbb{N}$, $T\geq1$, we draw samples from the $K$ distributions to get *data*: $\forall t, r_k(t) \sim \nu_k$, ie, $\mathbb{P}(r_k(t) = 1) = \mu_k$ and $r_k(t) \in \{0,1\}$.

# ## Generating stationary data
# 
# Here we give some examples of stationary problems and examples of data we can draw from them.

# In[6]:


def bernoulli_samples(means, horizon=1000):
    if np.size(means) == 1:
        return np.random.binomial(1, means, size=horizon)
    else:
        results = np.zeros((np.size(means), horizon))
        for i, mean in enumerate(means):
            results[i] = np.random.binomial(1, mean, size=horizon)
        return results


# In[7]:


problem1 = [0.5]

bernoulli_samples(problem1, horizon=20)


# In[100]:


sigma = 0.25  # Bernoulli are 1/4-sub Gaussian too!


# In[101]:


def gaussian_samples(means, horizon=1000, sigma=sigma):
    if np.size(means) == 1:
        return np.random.normal(loc=means, scale=sigma, size=horizon)
    else:
        results = np.zeros((np.size(means), horizon))
        for i, mean in enumerate(means):
            results[i] = np.random.normal(loc=mean, scale=sigma, size=horizon)
        return results


# In[102]:


gaussian_samples(problem1, horizon=20)


# For bandit problem with $K \geq 2$ arms, the *goal* is to design an online learning algorithm that roughly do the following:
# 
# - For time $t=1$ to $t=T$ (unknown horizon)
#     1. Algorithm $A$ decide to draw arm $A(t) \in\{1,\dots,K\}$,
#     2. Get the reward $r(t) = r_{A(t)}(t) \sim \nu_{A(t)}$ from the (Bernoulli) distribution of that arm,
#     3. Give this observation of reward $r(t)$ coming from arm $A(t)$ to the algorithm,
#     4. Update internal state of the algorithm
# 
# An algorithm is efficient if it obtains a high (expected) sum reward, ie, $\sum_{t=1}^T r(t)$.
# 
# Note that I don't focus on bandit algorithm here.

# In[8]:


problem2 = [0.1, 0.5, 0.9]

bernoulli_samples(problem2, horizon=20)


# In[103]:


problem2 = [0.1, 0.5, 0.9]

gaussian_samples(problem2, horizon=20)


# For instance on these data, the best arm is clearly the third one, with expected reward of $\mu^* = \max_k \mu_k = 0.9$.

# ## Mathematical notations for piecewise stationary problems
# 
# Now we fix the horizon $T\in\mathbb{N}$, $T\geq1$ and we also consider a set of $\Upsilon_T$ *break points*, $\tau_1,\dots,\tau_{\Upsilon_T} \in\{1,\dots,T\}$. We denote $\tau_0 = 0$ and $\tau_{\Upsilon_T+1} = T$ for convenience of notations.
# We can assume that breakpoints are far "enough" from each other, for instance that there exists an integer $N\in\mathbb{N},N\geq1$ such that $\min_{i=0}^{\Upsilon_T} \tau_{i+1} - \tau_i \geq N K$. That is, on each *stationary interval*, a uniform sampling of the $K$ arms gives at least $N$ samples by arm.
# 
# Now, in any stationary interval $[\tau_i + 1, \tau_{i+1}]$, the $K \geq 1$ arms are distributions $\nu_k^{(i)}$.
# We focus on Bernoulli distributions, which are characterized by their means, $\nu_k^{(i)} := \mathcal{B}(\mu_k^{(i)})$ for $\mu_k^{(i)}\in[0,1]$.
# A piecewise stationary bandit problem is defined here by the vector $[\mu_k^{(i)}]_{1\leq k \leq K, 1 \leq i \leq \Upsilon_T}$.
# 
# For a fixed problem and a *horizon* $T\in\mathbb{N}$, $T\geq1$, we draw samples from the $K$ distributions to get *data*: $\forall t, r_k(t) \sim \nu_k^{(i)}$ for $i$ the unique index of stationary interval such that $t\in[\tau_i + 1, \tau_{i+1}]$.

# ## Generating fake piecewise stationary data
# 
# The format to define piecewise stationary problem will be the following. It is compact but generic!
# 
# The first example considers a unique arm, with 2 breakpoints uniformly spaced.
# - On the first interval, for instance from $t=1$ to $t=500$, that is $\tau_1 = 500$, $\mu_1^{(1)} = 0.1$,
# - On the second interval, for instance from $t=501$ to $t=1000$, that is $\tau_2 = 100$, $\mu_1^{(2)} = 0.5$,
# - On the third interval, for instance from $t=1001$ to $t=1500$, that $\mu_1^{(3)} = 0.9$.

# In[9]:


# With 1 arm only!
problem_piecewise_0 = lambda horizon: {
    "listOfMeans": [
        [0.1],  # 0    to 499
        [0.5],  # 500  to 999
        [0.8],  # 1000  to 1499
    ],
    "changePoints": [
        int(0    * horizon / 1500.0),
        int(500  * horizon / 1500.0),
        int(1000  * horizon / 1500.0),
    ],
}


# In[10]:


# With 2 arms
problem_piecewise_1 = lambda horizon: {
    "listOfMeans": [
        [0.1, 0.2],  # 0    to 399
        [0.1, 0.3],  # 400  to 799
        [0.5, 0.3],  # 800  to 1199
        [0.4, 0.3],  # 1200 to 1599
        [0.3, 0.9],  # 1600 to end
    ],
    "changePoints": [
        int(0    * horizon / 2000.0),
        int(400  * horizon / 2000.0),
        int(800  * horizon / 2000.0),
        int(1200 * horizon / 2000.0),
        int(1600 * horizon / 2000.0),
    ],
}


# In[11]:


# With 3 arms
problem_piecewise_2 = lambda horizon: {
    "listOfMeans": [
        [0.2, 0.5, 0.9],  # 0    to 399
        [0.2, 0.2, 0.9],  # 400  to 799
        [0.2, 0.2, 0.1],  # 800  to 1199
        [0.7, 0.2, 0.1],  # 1200 to 1599
        [0.7, 0.5, 0.1],  # 1600 to end
    ],
    "changePoints": [
        int(0    * horizon / 2000.0),
        int(400  * horizon / 2000.0),
        int(800  * horizon / 2000.0),
        int(1200 * horizon / 2000.0),
        int(1600 * horizon / 2000.0),
    ],
}


# In[12]:


# With 3 arms
problem_piecewise_3 = lambda horizon: {
    "listOfMeans": [
        [0.4, 0.5, 0.9],  # 0    to 399
        [0.5, 0.4, 0.7],  # 400  to 799
        [0.6, 0.3, 0.5],  # 800  to 1199
        [0.7, 0.2, 0.3],  # 1200 to 1599
        [0.8, 0.1, 0.1],  # 1600 to end
    ],
    "changePoints": [
        int(0    * horizon / 2000.0),
        int(400  * horizon / 2000.0),
        int(800  * horizon / 2000.0),
        int(1200 * horizon / 2000.0),
        int(1600 * horizon / 2000.0),
    ],
}


# Now we can write a utility function that transform this compact representation into a full list of means.

# In[13]:


def getFullHistoryOfMeans(problem, horizon=2000):
    """Return the vector of mean of the arms, for a piece-wise stationary MAB.

    - It is a numpy array of shape (nbArms, horizon).
    """
    pb = problem(horizon)
    listOfMeans, changePoints = pb['listOfMeans'], pb['changePoints']
    nbArms = len(listOfMeans[0])
    if horizon is None:
        horizon = np.max(changePoints)
    meansOfArms = np.ones((nbArms, horizon))
    for armId in range(nbArms):
        nbChangePoint = 0
        for t in range(horizon):
            if nbChangePoint < len(changePoints) - 1 and t >= changePoints[nbChangePoint + 1]:
                nbChangePoint += 1
            meansOfArms[armId][t] = listOfMeans[nbChangePoint][armId]
    return meansOfArms


# For examples :

# In[14]:


getFullHistoryOfMeans(problem_piecewise_0, horizon=50)


# In[15]:


getFullHistoryOfMeans(problem_piecewise_1, horizon=50)


# In[16]:


getFullHistoryOfMeans(problem_piecewise_2, horizon=50)


# In[17]:


getFullHistoryOfMeans(problem_piecewise_3, horizon=50)


# And now we need to be able to generate samples from such distributions.

# In[18]:


def piecewise_bernoulli_samples(problem, horizon=1000):
    fullMeans = getFullHistoryOfMeans(problem, horizon=horizon)
    nbArms, horizon = np.shape(fullMeans)
    results = np.zeros((nbArms, horizon))
    for i in range(nbArms):
        mean_i = fullMeans[i, :]
        for t in range(horizon):
            mean_i_t = mean_i[t]
            results[i, t] = np.random.binomial(1, mean_i_t)
    return results


# In[104]:


def piecewise_gaussian_samples(problem, horizon=1000, sigma=sigma):
    fullMeans = getFullHistoryOfMeans(problem, horizon=horizon)
    nbArms, horizon = np.shape(fullMeans)
    results = np.zeros((nbArms, horizon))
    for i in range(nbArms):
        mean_i = fullMeans[i, :]
        for t in range(horizon):
            mean_i_t = mean_i[t]
            results[i, t] = np.random.normal(loc=mean_i_t, scale=sigma, size=1)
    return results


# Examples:

# In[19]:


getFullHistoryOfMeans(problem_piecewise_0, horizon=100)
piecewise_bernoulli_samples(problem_piecewise_0, horizon=100)


# In[105]:


piecewise_gaussian_samples(problem_piecewise_0, horizon=100)


# We easily spot the (approximate) location of the breakpoint!
# 
# Another example:

# In[20]:


piecewise_bernoulli_samples(problem_piecewise_1, horizon=100)


# In[107]:


piecewise_gaussian_samples(problem_piecewise_1, horizon=20)


# ----
# # Python implementations of some statistical tests
# 
# I will implement here the following statistical tests (and I give a link to the implementation of the correspond bandit policy in my framework [`SMPyBandits`](https://smpybandits.github.io/)
# 
# - Monitored (based on a McDiarmid inequality), for Monitored-UCB or [`M-UCB`](),
# - CUSUM, for [`CUSUM-UCB`](https://smpybandits.github.io/docs/Policies.CD_UCB.html?highlight=cusum#Policies.CD_UCB.CUSUM_IndexPolicy),
# - PHT, for [`PHT-UCB`](https://smpybandits.github.io/docs/Policies.CD_UCB.html?highlight=cusum#Policies.CD_UCB.PHT_IndexPolicy),
# - Gaussian GLR, for [`GaussianGLR-UCB`](https://smpybandits.github.io/docs/Policies.CD_UCB.html?highlight=glr#Policies.CD_UCB.GaussianGLR_IndexPolicy),
# - Bernoulli GLR, for [`BernoulliGLR-UCB`](https://smpybandits.github.io/docs/Policies.CD_UCB.html?highlight=glr#Policies.CD_UCB.BernoulliGLR_IndexPolicy).

# ## A stupid detection test (pure random!)
# Just to be sure that the test functions work as wanted, I start by writing a stupid change detection test, which is purely random!

# In[21]:


probaOfDetection = 0.05

delay = int(np.ceil(1.0 / probaOfDetection))
print(f"For a fixed probability of detection = {probaOfDetection}, the PurelyRandom algorithm has a mean delay of {delay} steps.")


# In[22]:


def PurelyRandom(all_data, t, proba=probaOfDetection):
    """ Delay will be ceil(1/proba) (in average)."""
    return np.random.random() < proba


# ## Monitored
# 
# It uses a McDiarmid inequality. At time $t$, if there is at least $w$ data in the data vector $(X_i)_i$, then let $Y$ denote the last $w$ data.
# A change is detected if
# $$ |\sum_{i=w/2+1}^{w} Y_i - \sum_{i=1}^{w/2} Y_i | > b ? $$

# In[23]:


NB_ARMS = 1
WINDOW_SIZE = 80


# In[24]:


def Monitored(all_data, t,
              window_size=WINDOW_SIZE, threshold_b=None,
    ):
    r""" A change is detected for the current arm if the following test is true:

    .. math:: |\sum_{i=w/2+1}^{w} Y_i - \sum_{i=1}^{w/2} Y_i | > b ?

    - where :math:`Y_i` is the i-th data in the latest w data from this arm (ie, :math:`X_k(t)` for :math:`t = n_k - w + 1` to :math:`t = n_k` current number of samples from arm k).
    - where :attr:`threshold_b` is the threshold b of the test, and :attr:`window_size` is the window-size w.
    """
    data = all_data[:t]
    # don't try to detect change if there is not enough data!
    if len(data) < window_size:
        return False
    
    # compute parameters
    horizon = len(all_data)
    if threshold_b is None:
        threshold_b = np.sqrt(window_size/2 * np.log(2 * NB_ARMS * horizon**2))

    last_w_data = data[-window_size:]
    sum_first_half = np.sum(last_w_data[:window_size//2])
    sum_second_half = np.sum(last_w_data[window_size//2:])
    return abs(sum_first_half - sum_second_half) > threshold_b


# ## CUSUM
# 
# The two-sided CUSUM algorithm, from [Page, 1954], works like this:
# 
# - For each *data* k, compute:
# 
# $$
# s_k^- = (y_k - \hat{u}_0 - \varepsilon) 1(k > M),\\
# s_k^+ = (\hat{u}_0 - y_k - \varepsilon) 1(k > M),\\
# g_k^+ = max(0, g_{k-1}^+ + s_k^+),\\
# g_k^- = max(0, g_{k-1}^- + s_k^-).
# $$
# 
# - The change is detected if $\max(g_k^+, g_k^-) > h$, where $h=$`threshold_h` is the threshold of the test,
# - And $\hat{u}_0 = \frac{1}{M} \sum_{k=1}^{M} y_k$ is the mean of the first M samples, where M is `M` the min number of observation between change points.

# In[25]:


#: Precision of the test.
EPSILON = 0.5

#: Default value of :math:`\lambda`.
LAMBDA = 1

#: Hypothesis on the speed of changes: between two change points, there is at least :math:`M * K` time steps, where K is the number of arms, and M is this constant.
MIN_NUMBER_OF_OBSERVATION_BETWEEN_CHANGE_POINT = 100

MAX_NB_RANDOM_EVENTS = 1


# In[26]:


from scipy.special import comb


# In[27]:


def compute_h__CUSUM(horizon, 
        verbose=False,
        M=MIN_NUMBER_OF_OBSERVATION_BETWEEN_CHANGE_POINT,
        max_nb_random_events=MAX_NB_RANDOM_EVENTS,
        nbArms=1,
        epsilon=EPSILON,
        lmbda=LAMBDA,
    ):
    r""" Compute the values :math:`C_1^+, C_1^-, C_1, C_2, h` from the formulas in Theorem 2 and Corollary 2 in the paper."""
    T = int(max(1, horizon))
    UpsilonT = int(max(1, max_nb_random_events))
    K = int(max(1, nbArms))
    C1_minus = np.log(((4 * epsilon) / (1-epsilon)**2) * comb(M, int(np.floor(2 * epsilon * M))) * (2 * epsilon)**M + 1)
    C1_plus = np.log(((4 * epsilon) / (1+epsilon)**2) * comb(M, int(np.ceil(2 * epsilon * M))) * (2 * epsilon)**M + 1)
    C1 = min(C1_minus, C1_plus)
    if C1 == 0: C1 = 1  # FIXME
    h = 1/C1 * np.log(T / UpsilonT)
    return h


# In[28]:


def CUSUM(all_data, t,
          epsilon=EPSILON,
          M=MIN_NUMBER_OF_OBSERVATION_BETWEEN_CHANGE_POINT,
          threshold_h=None,
    ):
    r""" Detect a change in the current arm, using the two-sided CUSUM algorithm [Page, 1954].

    - For each *data* k, compute:

    .. math::

        s_k^- &= (y_k - \hat{u}_0 - \varepsilon) 1(k > M),\\
        s_k^+ &= (\hat{u}_0 - y_k - \varepsilon) 1(k > M),\\
        g_k^+ &= max(0, g_{k-1}^+ + s_k^+),\\
        g_k^- &= max(0, g_{k-1}^- + s_k^-).

    - The change is detected if :math:`\max(g_k^+, g_k^-) > h`, where :attr:`threshold_h` is the threshold of the test,
    - And :math:`\hat{u}_0 = \frac{1}{M} \sum_{k=1}^{M} y_k` is the mean of the first M samples, where M is :attr:`M` the min number of observation between change points.
    """
    data = all_data[:t]
    
    # compute parameters
    horizon = len(all_data)
    if threshold_h is None:
        threshold_h = compute_h__CUSUM(horizon, M, 1, epsilon=epsilon)

    gp, gm = 0, 0
    # First we use the first M samples to calculate the average :math:`\hat{u_0}`.
    u0hat = np.mean(data[:M])
    for k, y_k in enumerate(data):
        if k <= M:
            continue
        sp = u0hat - y_k - epsilon  # no need to multiply by (k > self.M)
        sm = y_k - u0hat - epsilon  # no need to multiply by (k > self.M)
        gp, gm = max(0, gp + sp), max(0, gm + sm)
        if max(gp, gm) >= threshold_h:
            return True
    return False


# ## PHT
# 
# The two-sided CUSPHTUM algorithm, from [Hinkley, 1971], works like this:
# 
# - For each *data* k, compute:
# 
# $$
# s_k^- = y_k - \hat{y}_k - \varepsilon,\\
# s_k^+ = \hat{y}_k - y_k - \varepsilon,\\
# g_k^+ = max(0, g_{k-1}^+ + s_k^+),\\
# g_k^- = max(0, g_{k-1}^- + s_k^-).
# $$
# 
# - The change is detected if $\max(g_k^+, g_k^-) > h$, where $h=$`threshold_h` is the threshold of the test,
# - And $\hat{y}_k = \frac{1}{k} \sum_{s=1}^{k} y_s$ is the mean of the first k samples.

# In[29]:


def PHT(all_data, t,
          epsilon=EPSILON,
          M=MIN_NUMBER_OF_OBSERVATION_BETWEEN_CHANGE_POINT,
          threshold_h=None,
    ):
    r""" Detect a change in the current arm, using the two-sided PHT algorithm [Hinkley, 1971].

    - For each *data* k, compute:

    .. math::

        s_k^- &= y_k - \hat{y}_k - \varepsilon,\\
        s_k^+ &= \hat{y}_k - y_k - \varepsilon,\\
        g_k^+ &= max(0, g_{k-1}^+ + s_k^+),\\
        g_k^- &= max(0, g_{k-1}^- + s_k^-).

    - The change is detected if :math:`\max(g_k^+, g_k^-) > h`, where :attr:`threshold_h` is the threshold of the test,
    - And :math:`\hat{y}_k = \frac{1}{k} \sum_{s=1}^{k} y_s` is the mean of the first k samples.
    """
    data = all_data[:t]
    
    # compute parameters
    horizon = len(all_data)
    if threshold_h is None:
        threshold_h = compute_h__CUSUM(horizon, M, 1, epsilon=epsilon)

    gp, gm = 0, 0
    # First we use the first M samples to calculate the average :math:`\hat{u_0}`.
    for k, y_k in enumerate(data):
        y_k_hat = np.mean(data[:k])
        sp = y_k_hat - y_k - epsilon
        sm = y_k - y_k_hat - epsilon
        gp, gm = max(0, gp + sp), max(0, gm + sm)
        if max(gp, gm) >= threshold_h:
            return True
    return False


# ---
# ## Gaussian GLR
# 
# The Generalized Likelihood Ratio test (GLR) works with a one-dimensional exponential family, for which we have a function `kl` such that if $\mu_1,\mu_2$ are the means fo two distributions $\nu_1,\nu_2$, then $\mathrm{KL}(\mathcal{D}(\nu_1), \mathcal{D}(\nu_1))=$ `kl` $(\mu_1,\mu_2)$.
# 
# - For each *time step* $s$ between $t_0=0$ and $t$, compute:
# $$G^{\mathcal{N}_1}_{t_0:s:t} = \frac{(s-t_0+1)(t-s)}{(t-t_0+1)} \mathrm{kl}(\mu_{s+1,t}, \mu_{t_0,s}).$$
# 
# - The change is detected if there is a time $s$ such that $G^{\mathcal{N}_1}_{t_0:s:t} > h$, where $h=$ `threshold_h` is the threshold of the test,
# - And $\mu_{a,b} = \frac{1}{b-a+1} \sum_{s=a}^{b} y_s$ is the mean of the samples between $a$ and $b$.
# 
# The threshold is computed as:
# $$h := \left(1 + \frac{1}{t - t_0 + 1}\right) 2 \log\left(\frac{2 (t - t_0) \sqrt{(t - t_0) + 2}}{\delta}\right).$$

# In[30]:


def compute_c__GLR(t0, t, horizon):
    r""" Compute the values :math:`c, \alpha` from the corollary of of Theorem 2 from ["Sequential change-point detection: Laplace concentration of scan statistics and non-asymptotic delay bounds", O.-A. Maillard, 2018].

    - The threshold is computed as:

    .. math:: h := \left(1 + \frac{1}{t - t_0 + 1}\right) 2 \log\left(\frac{2 (t - t_0) \sqrt{(t - t_0) + 2}}{\delta}\right).
    """
    T = int(max(1, horizon))
    delta = 1.0 / T
    t_m_t0 = abs(t - t0)
    c = (1 + (1 / (t_m_t0 + 1.0))) * 2 * np.log((2 * t_m_t0 * np.sqrt(t_m_t0 + 2)) / delta)
    if c < 0 and np.isinf(c): c = float('+inf')
    return c


# For Gaussian distributions of known variance, the Kullback-Leibler divergence is easy to compute:
# 
# Kullback-Leibler divergence for Gaussian distributions of means $x$ and $y$ and variances $\sigma^2_x = \sigma^2_y$, $\nu_1 = \mathcal{N}(x, \sigma_x^2)$ and $\nu_2 = \mathcal{N}(y, \sigma_x^2)$ is:
# 
# $$\mathrm{KL}(\nu_1, \nu_2) = \frac{(x - y)^2}{2 \sigma_y^2} + \frac{1}{2}\left( \frac{\sigma_x^2}{\sigma_y^2} - 1 \log\left(\frac{\sigma_x^2}{\sigma_y^2}\right) \right).$$

# In[31]:


def klGauss(x, y, sig2x=0.25):
    r""" Kullback-Leibler divergence for Gaussian distributions of means ``x`` and ``y`` and variances ``sig2x`` and ``sig2y``, :math:`\nu_1 = \mathcal{N}(x, \sigma_x^2)` and :math:`\nu_2 = \mathcal{N}(y, \sigma_x^2)`:

    .. math:: \mathrm{KL}(\nu_1, \nu_2) = \frac{(x - y)^2}{2 \sigma_y^2} + \frac{1}{2}\left( \frac{\sigma_x^2}{\sigma_y^2} - 1 \log\left(\frac{\sigma_x^2}{\sigma_y^2}\right) \right).

    See https://en.wikipedia.org/wiki/Normal_distribution#Other_properties

    - sig2y = sig2x (same variance).
    """
    return (x - y) ** 2 / (2. * sig2x)


# In[32]:


def GaussianGLR(all_data, t,
          threshold_h=None,
    ):
    r""" Detect a change in the current arm, using the Generalized Likelihood Ratio test (GLR) and the :attr:`kl` function.

        - For each *time step* :math:`s` between :math:`t_0=0` and :math:`t`, compute:

        .. math::

            G^{\mathcal{N}_1}_{t_0:s:t} = (s-t_0+1)(t-s) \mathrm{kl}(\mu_{s+1,t}, \mu_{t_0,s}) / (t-t_0+1).

        - The change is detected if there is a time :math:`s` such that :math:`G^{\mathcal{N}_1}_{t_0:s:t} > h`, where :attr:`threshold_h` is the threshold of the test,
        - And :math:`\mu_{a,b} = \frac{1}{b-a+1} \sum_{s=a}^{b} y_s` is the mean of the samples between :math:`a` and :math:`b`.
    """
    data = all_data[:t]
    t0 = 0
    horizon = len(all_data)
    
    # compute parameters
    if threshold_h is None:
        threshold_h = compute_c__GLR(0, t, horizon)

    mu = lambda a, b: np.mean(data[a : b+1])
    for s in range(t0, t - 1):
        this_kl = klGauss(mu(s+1, t), mu(t0, s))
        glr = ((s - t0 + 1) * (t - s) / (t - t0 + 1)) * this_kl
        if glr >= threshold_h:
            return True
    return False


# ## Bernoulli GLR
# 
# The same GLR algorithm but using the Bernoulli KL, given by:
# 
# $$\mathrm{KL}(\mathcal{B}(x), \mathcal{B}(y)) = x \log(\frac{x}{y}) + (1-x) \log(\frac{1-x}{1-y}).$$

# In[33]:


eps = 1e-6  #: Threshold value: everything in [0, 1] is truncated to [eps, 1 - eps]

def klBern(x, y):
    r""" Kullback-Leibler divergence for Bernoulli distributions. https://en.wikipedia.org/wiki/Bernoulli_distribution#Kullback.E2.80.93Leibler_divergence

    .. math:: \mathrm{KL}(\mathcal{B}(x), \mathcal{B}(y)) = x \log(\frac{x}{y}) + (1-x) \log(\frac{1-x}{1-y})."""
    x = min(max(x, eps), 1 - eps)
    y = min(max(y, eps), 1 - eps)
    return x * np.log(x / y) + (1 - x) * np.log((1 - x) / (1 - y))


# In[34]:


def BernoulliGLR(all_data, t,
          threshold_h=None,
    ):
    r""" Detect a change in the current arm, using the Generalized Likelihood Ratio test (GLR) and the :attr:`kl` function.

        - For each *time step* :math:`s` between :math:`t_0=0` and :math:`t`, compute:

        .. math::

            G^{\mathcal{N}_1}_{t_0:s:t} = (s-t_0+1)(t-s) \mathrm{kl}(\mu_{s+1,t}, \mu_{t_0,s}) / (t-t_0+1).

        - The change is detected if there is a time :math:`s` such that :math:`G^{\mathcal{N}_1}_{t_0:s:t} > h`, where :attr:`threshold_h` is the threshold of the test,
        - And :math:`\mu_{a,b} = \frac{1}{b-a+1} \sum_{s=a}^{b} y_s` is the mean of the samples between :math:`a` and :math:`b`.
    """
    data = all_data[:t]
    t0 = 0
    horizon = len(all_data)
    
    # compute parameters
    if threshold_h is None:
        threshold_h = compute_c__GLR(0, t, horizon)

    mu = lambda a, b: np.mean(data[a : b+1])
    for s in range(t0, t - 1):
        this_kl = klBern(mu(s+1, t), mu(t0, s))
        glr = ((s - t0 + 1) * (t - s) / (t - t0 + 1)) * this_kl
        if glr >= threshold_h:
            return True
    return False


# ## List of all Python algorithms

# In[35]:


all_CD_algorithms = [
    PurelyRandom,
    Monitored, CUSUM, PHT, GaussianGLR, BernoulliGLR
]


# ----
# # Numba implementations of some statistical tests
# 
# I should try to use the [`numba.jit`](https://numba.pydata.org/numba-doc/latest/reference/jit-compilation.html#numba.jit) decorator for some of the (simple) functions defined above.
# With some luck, the JIT compiler will give automatic speedup.

# In[36]:


import numba


# In[37]:


@numba.jit(nopython=True)
def klGauss_numba(x, y, sig2x=0.25):
    return (x - y) ** 2 / (2. * sig2x)


# In[38]:


def GaussianGLR_numba(all_data, t,
          threshold_h=None,
    ):
    r""" Detect a change in the current arm, using the Generalized Likelihood Ratio test (GLR) and the :attr:`kl` function.

    - For each *time step* :math:`s` between :math:`t_0=0` and :math:`t`, compute:

    .. math::

        G^{\mathcal{N}_1}_{t_0:s:t} = (s-t_0+1)(t-s) \mathrm{kl}(\mu_{s+1,t}, \mu_{t_0,s}) / (t-t_0+1).

    - The change is detected if there is a time :math:`s` such that :math:`G^{\mathcal{N}_1}_{t_0:s:t} > h`, where :attr:`threshold_h` is the threshold of the test,
    - And :math:`\mu_{a,b} = \frac{1}{b-a+1} \sum_{s=a}^{b} y_s` is the mean of the samples between :math:`a` and :math:`b`.
    """
    data = all_data[:t]
    t0 = 0
    horizon = len(all_data)
    
    # compute parameters
    if threshold_h is None:
        threshold_h = compute_c__GLR(0, t, horizon)

    mu = lambda a, b: np.mean(data[a : b+1])
    for s in range(t0, t - 1):
        this_kl = klGauss_numba(mu(s+1, t), mu(t0, s))
        glr = ((s - t0 + 1) * (t - s) / (t - t0 + 1)) * this_kl
        if glr >= threshold_h:
            return True
    return False


# In[39]:


@numba.jit(nopython=True)
def klBern_numba(x, y):
    x = min(max(x, eps), 1 - eps)
    y = min(max(y, eps), 1 - eps)
    return x * np.log(x / y) + (1 - x) * np.log((1 - x) / (1 - y))


# In[40]:


def BernoulliGLR_numba(all_data, t,
          threshold_h=None,
    ):
    r""" Detect a change in the current arm, using the Generalized Likelihood Ratio test (GLR) and the :attr:`kl` function.

    - For each *time step* :math:`s` between :math:`t_0=0` and :math:`t`, compute:

    .. math::

        G^{\mathcal{N}_1}_{t_0:s:t} = (s-t_0+1)(t-s) \mathrm{kl}(\mu_{s+1,t}, \mu_{t_0,s}) / (t-t_0+1).

    - The change is detected if there is a time :math:`s` such that :math:`G^{\mathcal{N}_1}_{t_0:s:t} > h`, where :attr:`threshold_h` is the threshold of the test,
    - And :math:`\mu_{a,b} = \frac{1}{b-a+1} \sum_{s=a}^{b} y_s` is the mean of the samples between :math:`a` and :math:`b`.
    """
    data = all_data[:t]
    t0 = 0
    horizon = len(all_data)
    
    # compute parameters
    if threshold_h is None:
        threshold_h = compute_c__GLR(0, t, horizon)

    mu = lambda a, b: np.mean(data[a : b+1])
    for s in range(t0, t - 1):
        this_kl = klBern_numba(mu(s+1, t), mu(t0, s))
        glr = ((s - t0 + 1) * (t - s) / (t - t0 + 1)) * this_kl
        if glr >= threshold_h:
            return True
    return False


# In[41]:


all_CD_algorithms_numba = [
    GaussianGLR_numba, BernoulliGLR_numba
]
# all_CD_algorithms += all_CD_algorithms_numba


# ## Some results
# In the tests below, when comparing the between the pure Python implementations and the numba optimized implementations, I observe the following results (for $T=1000$, $\mu^1=0.1$, $\mu^2=0.9$ and $\tau=\frac{1}{2}T$):
# 
# | Algorithm | Time   |
# |------|------|
# | GaussianGLR | $2.98$ seconds |
# | BernoulliGLR | $3.3$ seconds |
# | GaussianGLR with numba for `kl` | $9.22$ seconds |
# | BernoulliGLR with numba for `kl` | $2.36$ seconds |
# 
# My conclusions from some experiments are that this implementation with Numba is **not** more efficient than the naive Python implementation. So, let's forget about it!
# Speeding up just the `kl` function is not enough also.

# ----
# # Cython implementations of some statistical tests
# 
# I should try to use the [`%%cython`](https://cython.readthedocs.io/en/latest/src/quickstart/build.html#jupyter-notebook) magic for all the functions defined above.

# ## Speeding up just the `kl` functions

# In[42]:


get_ipython().run_line_magic('load_ext', 'cython')


# In[43]:


get_ipython().run_cell_magic('cython', '', '\ndef klGauss_cython(float x, float y, float sig2x=0.25) -> float:\n    return (x - y) ** 2 / (2. * sig2x)')


# In[44]:


def GaussianGLR_cython1(all_data, t,
          threshold_h=None,
    ):
    r""" Detect a change in the current arm, using the Generalized Likelihood Ratio test (GLR) and the :attr:`kl` function.

    - For each *time step* :math:`s` between :math:`t_0=0` and :math:`t`, compute:

    .. math::

        G^{\mathcal{N}_1}_{t_0:s:t} = (s-t_0+1)(t-s) \mathrm{kl}(\mu_{s+1,t}, \mu_{t_0,s}) / (t-t_0+1).

    - The change is detected if there is a time :math:`s` such that :math:`G^{\mathcal{N}_1}_{t_0:s:t} > h`, where :attr:`threshold_h` is the threshold of the test,
    - And :math:`\mu_{a,b} = \frac{1}{b-a+1} \sum_{s=a}^{b} y_s` is the mean of the samples between :math:`a` and :math:`b`.
    """
    data = all_data[:t]
    t0 = 0
    horizon = len(all_data)
    
    # compute parameters
    if threshold_h is None:
        threshold_h, _ = compute_c_alpha__GLR(0, t, horizon)

    mu = lambda a, b: np.mean(data[a : b+1])
    for s in range(t0, t - 1):
        this_kl = klGauss_cython(mu(s+1, t), mu(t0, s))
        glr = ((s - t0 + 1) * (t - s) / (t - t0 + 1)) * this_kl
        if glr >= threshold_h:
            return True
    return False


# In[45]:


get_ipython().run_cell_magic('cython', '', 'from libc.math cimport log\neps = 1e-7  #: Threshold value: everything in [0, 1] is truncated to [eps, 1 - eps]\n\ndef klBern_cython(float x, float y) -> float:\n    x = min(max(x, eps), 1 - eps)\n    y = min(max(y, eps), 1 - eps)\n    return x * log(x / y) + (1 - x) * log((1 - x) / (1 - y))')


# In[46]:


def BernoulliGLR_cython1(all_data, t,
          threshold_h=None,
    ):
    r""" Detect a change in the current arm, using the Generalized Likelihood Ratio test (GLR) and the :attr:`kl` function.

    - For each *time step* :math:`s` between :math:`t_0=0` and :math:`t`, compute:

    .. math::

        G^{\mathcal{N}_1}_{t_0:s:t} = (s-t_0+1)(t-s) \mathrm{kl}(\mu_{s+1,t}, \mu_{t_0,s}) / (t-t_0+1).

    - The change is detected if there is a time :math:`s` such that :math:`G^{\mathcal{N}_1}_{t_0:s:t} > h`, where :attr:`threshold_h` is the threshold of the test,
    - And :math:`\mu_{a,b} = \frac{1}{b-a+1} \sum_{s=a}^{b} y_s` is the mean of the samples between :math:`a` and :math:`b`.
    """
    data = all_data[:t]
    t0 = 0
    horizon = len(all_data)
    
    # compute parameters
    if threshold_h is None:
        threshold_h, _ = compute_c_alpha__GLR(0, t, horizon)

    mu = lambda a, b: np.mean(data[a : b+1])
    for s in range(t0, t - 1):
        this_kl = klBern_cython(mu(s+1, t), mu(t0, s))
        glr = ((s - t0 + 1) * (t - s) / (t - t0 + 1)) * this_kl
        if glr >= threshold_h:
            return True
    return False


# With these two first versions, I observed, when comparing the between the pure Python implementations and these first naive cython optimized implementations, I observe the following results (for $T=1000$, $\mu^1=0.1$, $\mu^2=0.9$ and $\tau=\frac{1}{2}T$):
# 
# | Algorithm | Time   |
# |------|------|
# | GaussianGLR | $2.98$ seconds |
# | BernoulliGLR | $3.3$ seconds |
# | GaussianGLR with cython for `kl` | $2.83$ seconds |
# | BernoulliGLR with cython for `kl` | $2.26$ seconds |
# 
# Speeding up just the `kl` won't be enough, so I'll try to write the whole statistical test function in Cython cells.

# ## Speeding up the whole test functions
# 
# In the tests below, when comparing the different pure Python implementation, I observe the following results (for $T=1000$, $\mu^1=0.1$, $\mu^2=0.9$ and $\tau=\frac{1}{2}T$):
# 
# | Algorithm | Time   |
# |------|------|
# | Monitored | $0.0123$ seconds |
# | CUSUM | $0.543$ seconds |
# | <span style="color:red">PHT</span> | $2.97$ seconds |
# | <span style="color:red">GaussianGLR</span> | $2.98$ seconds |
# | <span style="color:red">BernoulliGLR</span> | $3.3$ seconds |
# 
# I will first try to write in Cython a PHT test and the two GLR tests.

# ### PHT in Cython

# The `scipy.special.comb` is not available from Cython, but by [reading its Cython `_comb.pyx`](https://github.com/scipy/scipy/blob/v1.1.0/scipy/special/_comb.pyx#L7) source code, we can write manually:

# Now, let's write a Cython version of the function that computes the threshold $h$.

# In[47]:


get_ipython().run_cell_magic('cython', '', 'from libc.math cimport log, floor, ceil\n\nEPSILON = 0.5\nLAMBDA = 1.0\nMIN_NUMBER_OF_OBSERVATION_BETWEEN_CHANGE_POINT = 100\nMAX_NB_RANDOM_EVENTS = 1\n\n#from scipy.special import comb  # unable to import from scipy.special\ncdef int comb_cython(int N, int k):\n    """ Manually defined scipy.special.comb function:\n    \n    comb(N, k) = {k choose N} number of combination of k elements among N."""\n    if k > N or N < 0 or k < 0:\n        return 0\n    cdef int M = N + 1\n    cdef int nterms = min(k, N - k)\n    cdef int numerator = 1\n    cdef int denominator = 1\n    cdef int j = 1\n    while j <= nterms:\n        numerator *= M - j\n        denominator *= j\n        j += 1\n    return numerator // denominator\n\ncdef float compute_h__CUSUM_cython(int horizon, \n        int M=MIN_NUMBER_OF_OBSERVATION_BETWEEN_CHANGE_POINT,\n        int nbArms=1,\n        float epsilon=EPSILON,\n        float lmbda=LAMBDA,\n        int max_nb_random_events=MAX_NB_RANDOM_EVENTS,\n    ):\n    r""" Compute the values :math:`C_1^+, C_1^-, C_1, C_2, h` from the formulas in Theorem 2 and Corollary 2 in the paper."""\n    cdef int T = int(max(1, horizon))\n    cdef int UpsilonT = int(max(1, max_nb_random_events))\n    cdef int K = int(max(1, nbArms))\n    cdef float C1_minus = log(((4.0 * epsilon) / (1.0-epsilon)**2) * comb_cython(M, int(floor(2.0 * epsilon * M))) * (2.0 * epsilon)**M + 1.0)\n    cdef float C1_plus = log(((4.0 * epsilon) / (1.0+epsilon)**2) * comb_cython(M, int(ceil(2.0 * epsilon * M))) * (2.0 * epsilon)**M + 1.0)\n    cdef float C1 = min(C1_minus, C1_plus)\n    if C1 == 0: C1 = 1.0  # FIXME\n    cdef float h = log(T / UpsilonT) / C1\n    return h\n\nimport numpy as np\ncimport numpy as np\nDTYPE = np.float\nctypedef np.float_t DTYPE_t\n\ndef PHT_cython(\n        np.ndarray[DTYPE_t, ndim=1] all_data,\n        int t,\n        float epsilon=EPSILON,\n        int M=MIN_NUMBER_OF_OBSERVATION_BETWEEN_CHANGE_POINT,\n    ) -> bool:\n    r""" Cython version of PHT. Detect a change in the current arm, using the two-sided PHT algorithm [Hinkley, 1971].\n\n        - For each *data* k, compute:\n\n        .. math::\n\n            s_k^- &= y_k - \\hat{y}_k - \\varepsilon,\\\\\n            s_k^+ &= \\hat{y}_k - y_k - \\varepsilon,\\\\\n            g_k^+ &= max(0, g_{k-1}^+ + s_k^+),\\\\\n            g_k^- &= max(0, g_{k-1}^- + s_k^-).\n\n        - The change is detected if :math:`\\max(g_k^+, g_k^-) > h`, where :attr:`threshold_h` is the threshold of the test,\n        - And :math:`\\hat{y}_k = \\frac{1}{k} \\sum_{s=1}^{k} y_s` is the mean of the first k samples.\n    """\n    assert all_data.dtype == DTYPE\n    cdef np.ndarray[DTYPE_t, ndim=1] data = all_data[:t]\n    # compute parameters\n    cdef int horizon = len(all_data)\n    cdef float threshold_h = compute_h__CUSUM_cython(horizon, M=M, nbArms=1, epsilon=epsilon)\n\n    cdef int k = 0\n    cdef int len_data = len(data)\n    cdef float gp = 0.0\n    cdef float gm = 0.0\n    cdef float y_k, y_k_hat\n    # First we use the first M samples to calculate the average :math:`\\hat{u_0}`.\n    while k < len_data:\n        y_k = data[k]\n        y_k_hat = np.mean(data[:k])\n        gp = max(0, gp + y_k_hat - y_k - epsilon)\n        gm = max(0, gm + y_k - y_k_hat - epsilon)\n        if gp >= threshold_h or gm >= threshold_h:\n            return True\n        k += 1\n    return False')


# ### Gaussian GLR in Cython

# In[49]:


get_ipython().run_cell_magic('cython', '', 'from libc.math cimport log, sqrt, isinf\n\ncdef float compute_c__GLR_cython(\n        int t0, int t, int horizon\n    ):\n    r""" Compute the values :math:`c, \\alpha` from the corollary of of Theorem 2 from ["Sequential change-point detection: Laplace concentration of scan statistics and non-asymptotic delay bounds", O.-A. Maillard, 2018].\n\n    - The threshold is computed as:\n\n    .. math:: h := \\left(1 + \\frac{1}{t - t_0 + 1}\\right) 2 \\log\\left(\\frac{2 (t - t_0) \\sqrt{(t - t_0) + 2}}{\\delta}\\right).\n    """\n    cdef float T = float(max(1, horizon))\n    cdef float t_m_t0 = float(abs(t - t0))\n    cdef float c = (1.0 + (1.0 / (t_m_t0 + 1.0))) * 2.0 * log(T * (2.0 * t_m_t0 * sqrt(t_m_t0 + 2.0)))\n    if c < 0 or isinf(c): c = float(\'+inf\')\n    return c\n\ncdef float klGauss_cython(float x, float y, float sig2x=0.25):\n    return (x - y) ** 2 / (2. * sig2x)\n\nimport numpy as np\ncimport numpy as np\nDTYPE = np.float\nctypedef np.float_t DTYPE_t\n\ndef GaussianGLR_cython(\n        np.ndarray[DTYPE_t, ndim=1] all_data,\n        int t,\n    ) -> bool:\n    r""" Cython version of GaussianGLR. Detect a change in the current arm, using the Generalized Likelihood Ratio test (GLR) and the :attr:`kl` function.\n\n        - For each *time step* :math:`s` between :math:`t_0=0` and :math:`t`, compute:\n\n        .. math::\n\n            G^{\\mathcal{N}_1}_{t_0:s:t} = (s-t_0+1)(t-s) \\mathrm{kl}(\\mu_{s+1,t}, \\mu_{t_0,s}) / (t-t_0+1).\n\n        - The change is detected if there is a time :math:`s` such that :math:`G^{\\mathcal{N}_1}_{t_0:s:t} > h`, where :attr:`threshold_h` is the threshold of the test,\n        - And :math:`\\mu_{a,b} = \\frac{1}{b-a+1} \\sum_{s=a}^{b} y_s` is the mean of the samples between :math:`a` and :math:`b`.\n    """\n    assert all_data.dtype == DTYPE\n    cdef np.ndarray[DTYPE_t, ndim=1] data = all_data[:t]\n    cdef int t0 = 0\n    cdef int horizon = len(all_data)\n    # compute parameters\n    cdef float threshold_h = compute_c__GLR_cython(0, t, horizon)\n\n    cdef this_kl, glr\n    cdef s = 0\n    while s < t:\n        this_kl = klGauss_cython(np.mean(data[s+1 : t+1]), np.mean(data[t0 : s+1]))\n        glr = ((s - t0 + 1) * (t - s) / (t - t0 + 1)) * this_kl\n        if glr >= threshold_h:\n            return True\n        s += 1\n    return False')


# ### Bernoulli GLR in Cython

# In[50]:


get_ipython().run_cell_magic('cython', '', 'from libc.math cimport log, sqrt, isinf\n\ncdef float compute_c__GLR_cython(\n        int t0, int t, int horizon\n    ):\n    r""" Compute the values :math:`c, \\alpha` from the corollary of of Theorem 2 from ["Sequential change-point detection: Laplace concentration of scan statistics and non-asymptotic delay bounds", O.-A. Maillard, 2018].\n\n    - The threshold is computed as:\n\n    .. math:: h := \\left(1 + \\frac{1}{t - t_0 + 1}\\right) 2 \\log\\left(\\frac{2 (t - t_0) \\sqrt{(t - t_0) + 2}}{\\delta}\\right).\n    """\n    cdef float T = float(max(1, horizon))\n    cdef float t_m_t0 = float(abs(t - t0))\n    cdef float c = (1.0 + (1.0 / (t_m_t0 + 1.0))) * 2.0 * log(T * (2.0 * t_m_t0 * sqrt(t_m_t0 + 2.0)))\n    if c < 0 or isinf(c): c = float(\'+inf\')\n    return c\n\neps = 1e-7\n\ncdef float klBern_cython(float x, float y):\n    x = min(max(x, eps), 1 - eps)\n    y = min(max(y, eps), 1 - eps)\n    return x * log(x / y) + (1 - x) * log((1 - x) / (1 - y))\n\nimport numpy as np\ncimport numpy as np\nDTYPE = np.float\nctypedef np.float_t DTYPE_t\n\ndef BernoulliGLR_cython(\n        np.ndarray[DTYPE_t, ndim=1] all_data,\n        int t,\n    ) -> bool:\n    r""" Cython version of BernoulliGLR. Detect a change in the current arm, using the Generalized Likelihood Ratio test (GLR) and the :attr:`kl` function.\n\n        - For each *time step* :math:`s` between :math:`t_0=0` and :math:`t`, compute:\n\n        .. math::\n\n            G^{\\mathcal{N}_1}_{t_0:s:t} = (s-t_0+1)(t-s) \\mathrm{kl}(\\mu_{s+1,t}, \\mu_{t_0,s}) / (t-t_0+1).\n\n        - The change is detected if there is a time :math:`s` such that :math:`G^{\\mathcal{N}_1}_{t_0:s:t} > h`, where :attr:`threshold_h` is the threshold of the test,\n        - And :math:`\\mu_{a,b} = \\frac{1}{b-a+1} \\sum_{s=a}^{b} y_s` is the mean of the samples between :math:`a` and :math:`b`.\n    """\n    assert all_data.dtype == DTYPE\n    cdef np.ndarray[DTYPE_t, ndim=1] data = all_data[:t]\n    cdef int t0 = 0\n    cdef int horizon = len(all_data)\n    # compute parameters\n    cdef float threshold_h = compute_c__GLR_cython(0, t, horizon)\n\n    cdef this_kl, glr\n    cdef s = 0\n    while s < t:\n        this_kl = klBern_cython(np.mean(data[s+1 : t+1]), np.mean(data[t0 : s+1]))\n        glr = ((s - t0 + 1) * (t - s) / (t - t0 + 1)) * this_kl\n        if glr >= threshold_h:\n            return True\n        s += 1\n    return False')


# ### Some results
# 
# With these two first versions, I observed, when comparing the between the pure Python implementations and these cython fully optimized implementations, I observe the following results (for $T=100$, $\mu^1=0.1$, $\mu^2=0.9$ and $\tau=\frac{1}{2}T$):
# 
# | Algorithm | Time   |
# |------|------|
# | BernoulliGLR | $0.0845$ seconds |
# | BernoulliGLR_cython | $0.0607$ seconds |
# | CUSUM | $0.00553$ seconds |
# | GaussianGLR | $0.0817$ seconds |
# | GaussianGLR_cython | $0.0832$ seconds |
# | Monitored | $0.00042$ seconds |
# | PHT | $0.0584$ seconds |
# | PHT_cython | $0.038$ seconds |
# | PurelyRandom | $0.000372$ seconds |

# I don't understand these results: how come the cython-optimized version of Gaussian GLR can be slower than the naive pure Python version?

# ### 3 more algorithms implemented in Cython

# In[51]:


all_CD_algorithms_cython = [
    PHT_cython, GaussianGLR_cython, BernoulliGLR_cython
]

# all_CD_algorithms += all_CD_algorithms_cython
all_CD_algorithms = [
    PurelyRandom,
    Monitored, CUSUM, PHT_cython, GaussianGLR, BernoulliGLR_cython,
]


# ----
# # Comparing the different implementations
# 
# I now want to compare, on a simple non stationary problem, the efficiency of the different change detection algorithms, in terms of:
# 
# - speed of computations (we should see that naive Python is much slower than Numba, which is also slower than the Cython version),
# - memory of algorithms? I guess we will draw the same observations,
# 
# But most importantly, in terms of:
# 
# - detection delay, as a function of the amplitude of the breakpoint, or number of prior data (from $t=1$ to $t=\tau$), or as a function of the parameter(s) of the algorithm,
# - probability of false detection, or missed detection.

# ## Generating some toy data

# In[52]:


# With 1 arm only! With 1 change only!
toy_problem_piecewise = lambda firstMean, secondMean, tau: lambda horizon: {
    "listOfMeans": [
        [firstMean],  # 0    to 499
        [secondMean],  # 500  to 999
    ],
    "changePoints": [
        0,
        tau
    ],
}


# In[108]:


def get_toy_data(firstMean=0.5, secondMean=0.9, tau=None, horizon=100, gaussian=False):
    if tau is None:
        tau = horizon // 2
    elif isinstance(tau, float):
        tau = int(tau * horizon)
    problem = toy_problem_piecewise(firstMean, secondMean, tau)
    if gaussian:
        data = piecewise_gaussian_samples(problem, horizon=horizon)
    else:
        data = piecewise_bernoulli_samples(problem, horizon=horizon)
    data = data.reshape(horizon)
    return data


# It is now very easy to get data and "see" manually on the data the location of the breakpoint:

# In[109]:


get_toy_data(firstMean=0.1, secondMean=0.9, tau=0.5, horizon=100)


# In[55]:


get_toy_data(firstMean=0.1, secondMean=0.9, tau=0.2, horizon=100)


# In[56]:


get_toy_data(firstMean=0.1, secondMean=0.4, tau=0.5, horizon=100)


# And similarly for Gaussian data, we clearly see a difference around the middle of the vector:

# In[110]:


get_toy_data(firstMean=0.1, secondMean=0.9, tau=0.5, horizon=100, gaussian=True)


# Of course, we want to check that detecting the change becomes harder when:
# 
# - the gap $\Delta = |\mu^{(2)} - \mu^{(1)}|$ decreases,
# - the number of samples before the change decreases ($\tau$ decreases),
# - the number of samples after the change decreases ($T - \tau$ decreases).

# In[57]:


# Cf. https://stackoverflow.com/a/36313217/
from IPython.display import display, Markdown


# In[111]:


def check_onemeasure(measure, name,
                     firstMean=0.1,
                     secondMean=0.4,
                     tau=0.5,
                     horizon=100,
                     repetitions=50,
                     gaussian=False,
                     unit=""
    ):
    if isinstance(tau, float):
        tau = int(tau * horizon)
    print(f"\nGenerating toy {'Gaussian' if gaussian else 'Bernoulli'} data for mu^1 = {firstMean}, mu^2 = {secondMean}, tau = {tau} and horizon = {horizon}...")
    results = np.zeros((repetitions, len(all_CD_algorithms)))
    for rep in tqdm(range(repetitions), desc="Repetitions"):
        data = get_toy_data(firstMean=firstMean, secondMean=secondMean, tau=tau, horizon=horizon, gaussian=gaussian)
        for i, CDAlgorithm in enumerate(all_CD_algorithms):
            results[rep, i] = measure(data, tau, CDAlgorithm)
    # print and display a table of the results
    markdown_text = """
| Algorithm | {} |
|------|------|
{}
    """.format(name, "\n".join([
        "| {} | ${:.3g}${} |".format(CDAlgorithm.__name__, mean_result,unit)
        for CDAlgorithm, mean_result in zip(all_CD_algorithms, np.mean(results, axis=0))
    ]))
    print(markdown_text)
    display(Markdown(markdown_text))
    return results


# ## Checking time efficiency
# I don't really care about memory efficiency, so I won't check it.

# In[112]:


import time


# In[113]:


def time_efficiency(data, tau, CDAlgorithm):
    startTime = time.time()
    horizon = len(data)
    for t in range(0, horizon + 1):
        _ = CDAlgorithm(data, t)
    endTime = time.time()
    return endTime - startTime


# For examples:

# In[114]:


_ = check_onemeasure(time_efficiency, "Time", firstMean=0.1, secondMean=0.4, tau=0.5, horizon=100, unit=" seconds")


# In[115]:


_ = check_onemeasure(time_efficiency, "Time", firstMean=0.1, secondMean=0.4, tau=0.5, horizon=100, unit=" seconds", gaussian=True)


# <span style="color:red">`PHT` and the two `GLR` are very slow, compared to the `Monitored` approach, and slow compared to `CUSUM`!</span>

# In[99]:


get_ipython().run_cell_magic('time', '', '_ = check_onemeasure(time_efficiency, "Time", firstMean=0.1, secondMean=0.9, tau=0.5, horizon=1000, unit=" seconds")')


# <span style="color:red">`PHT` and the two `GLR` are very slow, compared to the `Monitored` approach, and slow compared to `CUSUM`!</span>

# ## Checking detection delay

# In[62]:


def detection_delay(data, tau, CDAlgorithm):
    horizon = len(data)
    if isinstance(tau, float): tau = int(tau * horizon)
    for t in range(tau, horizon + 1):
        if CDAlgorithm(data, t):
            return t - tau
    return horizon - tau


# Now we can check the detection delay for our different algorithms.

# For examples:

# In[108]:


_ = check_onemeasure(detection_delay, "Mean detection delay", firstMean=0.1, secondMean=0.4, tau=0.5, horizon=100)


# <span style="color:red">A lot of detection delay are large (ie. it was detected too late), with not enough data! `BernoulliGLR` seems to be the only one "fast enough"!</span>

# In[67]:


get_ipython().run_cell_magic('time', '', '_ = check_onemeasure(detection_delay, "Mean detection delay", firstMean=0.1, secondMean=0.9, tau=0.5, horizon=1000)')


# <span style="color:green">A very small detection delay, with enough data (a delay of 40 is *very* small when there is $500$ data of $\nu_1$ and $\nu_2$) !</span>

# ## Checking false alarm probabilities

# In[63]:


def false_alarm(data, tau, CDAlgorithm):
    horizon = len(data)
    if isinstance(tau, float): tau = int(tau * horizon)
    for t in range(0, tau):
        if CDAlgorithm(data, t):
            return True
    return False


# Now we can check the false alarm probabilities for our different algorithms.

# For examples:

# In[110]:


_ = check_onemeasure(false_alarm, "Mean false alarm rate", firstMean=0.1, secondMean=0.4, tau=0.5, horizon=100)


# <span style="color:red">A lot of false alarm for `BernoulliGLR` but not the others, with not enough data!</span>

# In[71]:


get_ipython().run_cell_magic('time', '', '_ = check_onemeasure(false_alarm, "Mean false alarm rate", firstMean=0.1, secondMean=0.9, tau=0.5, horizon=1000)')


# <span style="color:green">No false alarm, with enough data!</span>

# ## Checking missed detection probabilities

# In[64]:


def missed_detection(data, tau, CDAlgorithm):
    horizon = len(data)
    if isinstance(tau, float): tau = int(tau * horizon)
    for t in range(tau, horizon + 1):
        if CDAlgorithm(data, t):
            return False
    return True


# Now we can check the false alarm probabilities for our different algorithms.

# For examples:

# In[112]:


_ = check_onemeasure(missed_detection, "Mean missed detection rate", firstMean=0.1, secondMean=0.4, tau=0.5, horizon=100)


# <span style="color:red">A lot of missed detection, with not enough data!</span>

# In[113]:


get_ipython().run_cell_magic('time', '', '_ = check_onemeasure(missed_detection, "Mean missed detection rate", firstMean=0.1, secondMean=0.9, tau=0.5, horizon=1000)')


# <span style="color:green">No missed detection, with enough data!</span>

# ----
# # More simulations and some plots

# ## Run a check for a grid of values
# 
# Fix an algorithm, e.g., `Monitored`, then consider one of the quantities defined above (time efficiency, delay, false alarm or missed detection probas).
# Now, a piecewise stationary problem is characterized by the parameters $\mu_1$, $\Delta = |\mu_2 - \mu_1|$, and $\tau$ and $T$.
# 
# - Fix $\mu_1=\frac12$, and so $\Delta$ can be taken anywhere in $[0, \frac12]$.
# - Fix $T=1000$ for instance, and so $\tau$ can be taken anywhere in $[0,T]$.
# 
# Of course, if any of $\tau$ or $\Delta$ are too small, detection is impossible.
# I want to display a $2$D image view, showing on $x$-axis a grid of values of $\Delta$, on $y$-axis a grid of values of $\tau$, and on the $2$D image, a color-scale to show the detection delay (for instance).

# In[65]:


mu_1 = 0.5
max_mu_2 = 1
nb_values_Delta = 20
values_Delta = np.linspace(0, max_mu_2 - mu_1, nb_values_Delta)


# In[66]:


horizon = T = 5000
min_tau = 50
max_tau = T - min_tau
step = 50
values_tau = np.arange(min_tau, max_tau + 1, step)
nb_values_tau = len(values_tau)


# In[67]:


print(f"This will give a grid of {nb_values_Delta} x {nb_values_tau} = {nb_values_Delta * nb_values_tau} values of Delta and tau to explore.")


# And now the function:

# In[116]:


def check2D_onemeasure(measure,
                       CDAlgorithm,
                       values_Delta,
                       values_tau,
                       firstMean=mu_1,
                       horizon=horizon,
                       repetitions=10,
                       verbose=True,
                       gaussian=False,
                       n_jobs=1,
    ):
    print(f"\nExploring {measure.__name__} for algorithm {CDAlgorithm.__name__} mu^1 = {firstMean} and horizon = {horizon}...")
    nb_values_Delta = len(values_Delta)
    nb_values_tau = len(values_tau)
    print(f"with {nb_values_Delta} values for Delta, and {nb_values_tau} values for tau, and {repetitions} repetitions.")
    results = np.zeros((nb_values_Delta, nb_values_tau))
    
    for i, delta in tqdm(enumerate(values_Delta), desc="Delta s", leave=False):
        for j, tau in tqdm(enumerate(values_tau), desc="Tau s", leave=False):
            secondMean = firstMean + delta
            if isinstance(tau, float): tau = int(tau * horizon)
                
            # now the random Monte Carlo repetitions
            for rep in tqdm(range(repetitions), desc="Repetitions", leave=False):
                data = get_toy_data(firstMean=firstMean, secondMean=secondMean, tau=tau, horizon=horizon, gaussian=gaussian)
                result = measure(data, tau, CDAlgorithm)
                results[i, j] += result
            results[i, j] /= repetitions
            if verbose: print(f"For delta = {delta} ({i}th), tau = {tau} ({j}th), mean result = {results[i, j]}")
    return results


# ## A version using `joblib.Parallel` to use multi-core computations
# 
# I want to (try to) use [`joblib.Parallel`](https://joblib.readthedocs.io/en/latest/parallel.html) to run the "repetitions" for loop in parallel, for instance on 4 cores on my machine.

# In[69]:


from joblib import Parallel, delayed


# In[70]:


# Tries to know number of CPU
try:
    from multiprocessing import cpu_count
    CPU_COUNT = cpu_count()  #: Number of CPU on the local machine
except ImportError:
    CPU_COUNT = 1
print(f"Info: using {CPU_COUNT} jobs in parallel!")


# We can rewrite the `check2D_onemeasure` function to run some loops in parallel.

# In[119]:


def check2D_onemeasure_parallel(measure,
                                CDAlgorithm,
                                values_Delta,
                                values_tau,
                                firstMean=mu_1,
                                horizon=horizon,
                                repetitions=10,
                                verbose=1,
                                gaussian=False,
                                n_jobs=CPU_COUNT,
    ):
    print(f"\nExploring {measure.__name__} for algorithm {CDAlgorithm.__name__} mu^1 = {firstMean} and horizon = {horizon}...")
    nb_values_Delta = len(values_Delta)
    nb_values_tau = len(values_tau)
    print(f"with {nb_values_Delta} values for Delta, and {nb_values_tau} values for tau, and {repetitions} repetitions.")
    results = np.zeros((nb_values_Delta, nb_values_tau))

    def delayed_measure(i, delta, j, tau, rep):
        secondMean = firstMean + delta
        if isinstance(tau, float): tau = int(tau * horizon)
        data = get_toy_data(firstMean=firstMean, secondMean=secondMean, tau=tau, horizon=horizon, gaussian=gaussian)
        return i, j, measure(data, tau, CDAlgorithm)

    # now the random Monte Carlo repetitions
    for i, j, result in Parallel(n_jobs=n_jobs, verbose=int(verbose))(
        delayed(delayed_measure)(i, delta, j, tau, rep)
        for i, delta in tqdm(enumerate(values_Delta), desc="Delta s ||",    leave=False)
        for j, tau   in tqdm(enumerate(values_tau),   desc="Tau s ||",      leave=False)
        for rep      in tqdm(range(repetitions),      desc="Repetitions||", leave=False)
    ):
        results[i, j] += result
    results /= repetitions

    if verbose:
        for i, delta in enumerate(values_Delta):
            for j, tau in enumerate(values_tau):
                print(f"For delta = {delta} ({i}th), tau = {tau} ({j}th), mean result = {results[i, j]}")
    return results


# ## Checking on a small grid of values

# In[72]:


get_ipython().run_cell_magic('time', '', '_ = check2D_onemeasure(time_efficiency,\n                       Monitored,\n                       values_Delta=[0.05, 0.25, 0.5],\n                       values_tau=[1/10, 1/4, 2/4, 3/4, 9/10],\n                       firstMean=0.5,\n                       horizon=1000,\n                       repetitions=100)')


# In[73]:


get_ipython().run_cell_magic('time', '', '_ = check2D_onemeasure_parallel(time_efficiency,\n                                Monitored,\n                                values_Delta=[0.05, 0.25, 0.5],\n                                values_tau=[1/10, 1/4, 2/4, 3/4, 9/10],\n                                firstMean=0.5,\n                                horizon=1000,\n                                repetitions=100,\n                                n_jobs=4)')


# In[74]:


get_ipython().run_cell_magic('time', '', '_ = check2D_onemeasure(detection_delay,\n                       Monitored,\n                       values_Delta=[0.05, 0.25, 0.5],\n                       values_tau=[1/10, 1/4, 2/4, 3/4, 9/10],\n                       firstMean=0.5,\n                       horizon=1000,\n                       repetitions=100)')


# In[75]:


get_ipython().run_cell_magic('time', '', '_ = check2D_onemeasure_parallel(detection_delay,\n                                Monitored,\n                                values_Delta=[0.05, 0.25, 0.5],\n                                values_tau=[1/10, 1/4, 2/4, 3/4, 9/10],\n                                firstMean=0.5,\n                                horizon=1000,\n                                repetitions=100\n                               )')


# In[76]:


get_ipython().run_cell_magic('time', '', '_ = check2D_onemeasure_parallel(false_alarm,\n                                Monitored,\n                                values_Delta=[0.05, 0.25, 0.5],\n                                values_tau=[1/10, 1/4, 2/4, 3/4, 9/10],\n                                firstMean=0.5,\n                                horizon=1000,\n                                repetitions=100,\n                                )')


# In[77]:


get_ipython().run_cell_magic('time', '', '_ = check2D_onemeasure_parallel(missed_detection,\n                                Monitored,\n                                values_Delta=[0.05, 0.25, 0.5],\n                                values_tau=[1/10, 1/4, 2/4, 3/4, 9/10],\n                                firstMean=0.5,\n                                horizon=1000,\n                                repetitions=100,\n                                )')


# ## Plotting the result as a 2D image

# In[78]:


import matplotlib as mpl
FIGSIZE = (19.80, 10.80)  #: Figure size, in inches!
mpl.rcParams['figure.figsize'] = FIGSIZE
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt    


# Now the function:

# In[122]:


def view2D_onemeasure(measure, name,
                      CDAlgorithm,
                      values_Delta,
                      values_tau,
                      firstMean=mu_1,
                      horizon=horizon,
                      repetitions=10,
                      gaussian=False,
                      n_jobs=CPU_COUNT,
    ):
    check = check2D_onemeasure_parallel if n_jobs > 1 else check2D_onemeasure
    results = check(measure, CDAlgorithm,
                    values_Delta, values_tau,
                    firstMean=firstMean, 
                    horizon=horizon,
                    repetitions=repetitions,
                    verbose=False,
                    gaussian=gaussian,
                    n_jobs=n_jobs,
    )
    fig = plt.figure()

    plt.matshow(results)
    plt.colorbar(shrink=0.7)

    plt.locator_params(axis='x', nbins=1+len(values_tau))
    plt.locator_params(axis='y', nbins=len(values_Delta))

    ax = plt.gca()
    # https://stackoverflow.com/a/19972993/
    loc = ticker.MultipleLocator(base=1.0) # this locator puts ticks at regular intervals
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_ticks_position('bottom')
    def y_fmt(tick_value, pos): return '{:.3g}'.format(tick_value)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(y_fmt))
    ax.yaxis.set_major_locator(loc)

    # hack to display the ticks labels as the actual values
    if np.max(values_tau) <= 1:
        values_tau = np.floor(np.asarray(values_tau) * horizon)
        values_tau = list(np.asarray(values_tau, dtype=int))
    values_Delta = np.round(values_Delta, 3)
    ax.set_xticklabels([0] + list(values_tau))  # hack: the first label is not displayed??
    ax.set_yticklabels([0] + list(values_Delta))  # hack: the first label is not displayed??

    plt.title(rf"{name} for algorithm {CDAlgorithm.__name__}, for $T={horizon}$, {'Gaussian' if gaussian else 'Bernoulli'} data and $\mu_1={firstMean:.3g}$ and ${repetitions}$ repetitions")
    plt.xlabel(r"Value of $\tau$ time of breakpoint")
    plt.ylabel(r"Value of gap $\Delta = |\mu_2 - \mu_1|$")

    return fig


# ### First example, for `Monitored`

# In[80]:


get_ipython().run_cell_magic('time', '', '_ = view2D_onemeasure(detection_delay, "Detection delay",\n                      Monitored,\n                      values_Delta=[0.05, 0.1, 0.25, 0.4, 0.5],\n                      values_tau=[1/10, 1/4, 2/4, 3/4, 9/10],\n                      firstMean=0.5,\n                      horizon=1000,\n                      repetitions=100,\n                     )')


# In[81]:


get_ipython().run_cell_magic('time', '', '_ = view2D_onemeasure(missed_detection, "Missed detection probability",\n                      Monitored,\n                      values_Delta=[0.05, 0.1, 0.25, 0.4, 0.5],\n                      values_tau=[1/10, 1/4, 2/4, 3/4, 9/10],\n                      firstMean=0.5,\n                      horizon=1000,\n                      repetitions=100,\n                     )')


# In[121]:


get_ipython().run_cell_magic('time', '', '_ = view2D_onemeasure(missed_detection, "Missed detection probability",\n                      Monitored,\n                      values_Delta=[0.05, 0.1, 0.25, 0.4, 0.5],\n                      values_tau=[1/10, 1/4, 2/4, 3/4, 9/10],\n                      firstMean=0.5,\n                      horizon=1000,\n                      repetitions=100,\n                      gaussian=True,\n                     )')


# ### For `CUSUM`

# In[82]:


get_ipython().run_cell_magic('time', '', '_ = view2D_onemeasure(detection_delay, "Detection delay",\n                      CUSUM,\n                      values_Delta=[0.05, 0.1, 0.25, 0.4, 0.5],\n                      values_tau=[1/10, 1/4, 2/4, 3/4, 9/10],\n                      firstMean=0.5,\n                      horizon=1000,\n                      repetitions=10,\n                     )')


# In[123]:


get_ipython().run_cell_magic('time', '', '_ = view2D_onemeasure(missed_detection, "Missed detection probability",\n                      CUSUM,\n                      values_Delta=[0.05, 0.1, 0.25, 0.4, 0.5],\n                      values_tau=[1/10, 1/4, 2/4, 3/4, 9/10],\n                      firstMean=0.5,\n                      horizon=1000,\n                      repetitions=10,\n                     )')


# ### Second example

# In[124]:


firstMean = mu_1 = 0.5
max_mu_2 = 1
nb_values_Delta = 10
max_delta = max_mu_2 - mu_1
epsilon = 0.03
values_Delta = np.linspace(epsilon * max_delta, (1 - epsilon) * max_delta, nb_values_Delta)
print(f"Values of delta: {values_Delta}")


# In[125]:


horizon = T = 1000
min_tau = 50
max_tau = T - min_tau
step = 100
values_tau = np.arange(min_tau, max_tau + 1, step)
nb_values_tau = len(values_tau)
print(f"Values of tau: {values_tau}")


# In[126]:


print(f"This will give a grid of {nb_values_Delta} x {nb_values_tau} = {nb_values_Delta * nb_values_tau} values of Delta and tau to explore.")


# In[86]:


get_ipython().run_cell_magic('time', '', '_ = view2D_onemeasure(detection_delay, "Detection delay",\n                      Monitored,\n                      values_Delta=values_Delta,\n                      values_tau=values_tau,\n                      firstMean=firstMean,\n                      horizon=horizon,\n                      repetitions=50,\n                     )')


# In[127]:


get_ipython().run_cell_magic('time', '', '_ = view2D_onemeasure(detection_delay, "Detection delay",\n                      Monitored,\n                      values_Delta=values_Delta,\n                      values_tau=values_tau,\n                      firstMean=firstMean,\n                      horizon=horizon,\n                      repetitions=50,\n                      gaussian=True,\n                     )')


# In[88]:


get_ipython().run_cell_magic('time', '', '_ = view2D_onemeasure(detection_delay, "Detection delay",\n                      CUSUM,\n                      values_Delta=values_Delta,\n                      values_tau=values_tau,\n                      firstMean=firstMean,\n                      horizon=horizon,\n                      repetitions=10,\n                     )')


# In[90]:


get_ipython().run_cell_magic('time', '', '_ = view2D_onemeasure(detection_delay, "Detection delay",\n                      PHT,\n                      values_Delta=values_Delta,\n                      values_tau=values_tau,\n                      firstMean=firstMean,\n                      horizon=horizon,\n                      repetitions=1,\n                     )')


# In[128]:


get_ipython().run_cell_magic('time', '', '_ = view2D_onemeasure(detection_delay, "Detection delay",\n                      BernoulliGLR,\n                      values_Delta=values_Delta,\n                      values_tau=values_tau,\n                      firstMean=firstMean,\n                      horizon=horizon,\n                      repetitions=1,\n                     )')


# In[129]:


get_ipython().run_cell_magic('time', '', '_ = view2D_onemeasure(detection_delay, "Detection delay",\n                      BernoulliGLR,\n                      values_Delta=values_Delta,\n                      values_tau=values_tau,\n                      firstMean=firstMean,\n                      horizon=horizon,\n                      repetitions=1,\n                      gaussian=True,\n                     )')


# <center><span style="font-size:xx-large; color:red;">TODO TODO TODO TODO TODO TODO</span></center>

# In[129]:


get_ipython().run_cell_magic('time', '', '_ = view2D_onemeasure(detection_delay, "Detection delay",\n                      GaussianGLR,\n                      values_Delta=values_Delta,\n                      values_tau=values_tau,\n                      firstMean=firstMean,\n                      horizon=horizon,\n                      repetitions=1,\n                     )')


# In[129]:


get_ipython().run_cell_magic('time', '', '_ = view2D_onemeasure(detection_delay, "Detection delay",\n                      GaussianGLR,\n                      values_Delta=values_Delta,\n                      values_tau=values_tau,\n                      firstMean=firstMean,\n                      horizon=horizon,\n                      repetitions=1,\n                      gaussian=True,\n                     )')


# ### More examples

# <center><span style="font-size:xx-large; color:red;">TODO TODO TODO TODO TODO TODO</span></center>

# ----
# # Conclusions

# <center><span style="font-size:xx-large; color:red;">TODO TODO TODO TODO TODO TODO</span></center>