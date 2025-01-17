import pickle
import numpy as np
import os
import random
import matplotlib.pyplot as plt

def sliding_window(data, N):
    """
    For each index, k, in data we average over the window from k-N-1 to k. The beginning handles incomplete buffers,
    that is it only takes the average over what has actually been seen.
    :param data: A numpy array, length M
    :param N: The length of the sliding window.
    :return: A numpy array, length M, containing smoothed averaging.
    """
    idx = 0
    window = np.zeros(N)
    smoothed = np.zeros(len(data))
    for i in range(len(data)):
        window[idx] = data[i]
        idx += 1
        smoothed[i] = window[0:idx].mean()
        if idx == N:
            window[0:-1] = window[1:]
            idx = N - 1
    return smoothed
'''
dir = 'runs_data_cartpole1_30runs/nobaseline/'
files = os.listdir(dir)
all_returns = []
for file in files:
    f = open(dir+file, 'rb')
    all_returns.append(pickle.load(f))
    f.close()

sampled_results = []

plt.figure(figsize=(12,8))
plt.title("Episode Return")
plt.xlabel("Episode")
plt.ylabel("Average Return (Sliding Window 100)")
window = 100    

runs = 3
#Q 1

for i in range(10):#change to 10 or 1
    result = np.zeros(len(all_returns[0]))
    for j in range(runs):
        result += np.array(all_returns[random.randint(0,29)])
    result /= runs
    result = list(result)
    #sampled_results.append(result)
    plt.plot(sliding_window(result, window), label='Run ' + str(i+1))

plt.legend()
plt.show()
'''
'''
#for i in range(10):
#    plt.plot(sliding_window(sampled_results[i], window))


#Q 2
'''
'''
for i in range(1):#change to 10 or 1
    result = np.zeros(len(all_returns[0]))
    for j in range(runs):
        result += np.array(all_returns[random.randint(0,29)])
    result /= runs
    result = list(result)
    sampled_results.append(result)
    plt.plot(sliding_window(result, window), label=str(runs)+' runs')
    
'''
'''
for i in range(1):#change to 10 or 1
    result = np.zeros(len(all_returns[0]))
    for j in range(runs):
        result += np.array(all_returns[j])
    result /= runs
    result = list(result)
    sampled_results.append(result)
    
    plt.plot(sliding_window(result, window), label=str(runs)+' runs')
    plt.fill_between(sliding_window(result + sigma, window), sliding_window(result - sigma, window), alpha=0.5)
'''
'''
plt.figure(figsize=(12,8))
plt.title("Episode Return")
plt.xlabel("Episode")
plt.ylabel("Average Return (Sliding Window 100)")
window = 100
runs = 3
episodes = [i for i in range(0,100)]
for i in range(1):
    sampled_results = []        
    for j in range(runs):
        #sampled_results.append(np.array(all_returns[j]))
        sampled_results.append(np.array(all_returns[random.randint(0,29)]))
    result_mean = []
    result_std = []
    for k in range(len(episodes)):
        samples = []
        for l in range(len(sampled_results)):
            samples.append(sampled_results[l][k])
        result_mean.append(np.mean(samples))
        result_std.append(np.std(samples))
    result_std = np.array(result_std)
    result_mean_p_std = result_mean + result_std
    result_mean_m_std = result_mean - result_std
    for k in range(len(result_mean_p_std)):
        if result_mean_p_std[k] >= 200:
            result_mean_p_std[k] = 200
        if result_mean_m_std[k] <= 0:
            result_mean_m_std[k] = 0
    plt.plot(episodes, sliding_window(list(result_mean), window), label=str(runs)+' runs')
    plt.fill_between(episodes, sliding_window(list(result_mean_p_std), window), sliding_window(list(result_mean_m_std),window), alpha=0.25)

    
runs = 10
episodes = [i for i in range(0,100)]
for i in range(1):
    sampled_results = []        
    for j in range(runs):
        #sampled_results.append(np.array(all_returns[j]))
        sampled_results.append(np.array(all_returns[random.randint(0,29)]))
    result_mean = []
    result_std = []
    for k in range(len(episodes)):
        samples = []
        for l in range(len(sampled_results)):
            samples.append(sampled_results[l][k])
        result_mean.append(np.mean(samples))
        result_std.append(np.std(samples))
    result_std = np.array(result_std)
    result_mean_p_std = result_mean + result_std
    result_mean_m_std = result_mean - result_std
    for k in range(len(result_mean_p_std)):
        if result_mean_p_std[k] >= 200:
            result_mean_p_std[k] = 200
        if result_mean_m_std[k] <= 0:
            result_mean_m_std[k] = 0
    plt.plot(episodes, sliding_window(list(result_mean), window), label=str(runs)+' runs')
    plt.fill_between(episodes, sliding_window(list(result_mean_p_std), window), sliding_window(list(result_mean_m_std),window), alpha=0.25)


runs = 30
episodes = [i for i in range(0,100)]
for i in range(1):
    sampled_results = []        
    for j in range(runs):
        sampled_results.append(np.array(all_returns[j]))
        #sampled_results.append(np.array(all_returns[random.randint(0,29)]))
    result_mean = []
    result_std = []
    for k in range(len(episodes)):
        samples = []
        for l in range(len(sampled_results)):
            samples.append(sampled_results[l][k])
        result_mean.append(np.mean(samples))
        result_std.append(np.std(samples))
    result_std = np.array(result_std)
    result_mean_p_std = result_mean + result_std
    result_mean_m_std = result_mean - result_std
    for k in range(len(result_mean_p_std)):
        if result_mean_p_std[k] >= 200:
            result_mean_p_std[k] = 200
        if result_mean_m_std[k] <= 0:
            result_mean_m_std[k] = 0
    plt.plot(episodes, sliding_window(list(result_mean), window), label=str(runs)+' runs')
    plt.fill_between(episodes, sliding_window(list(result_mean_p_std), window), sliding_window(list(result_mean_m_std),window), alpha=0.25)

plt.legend()
plt.show()
'''

dir = 'runs_data_cartpole1_50runs_new/testing/baseline/'
files = os.listdir(dir)
all_returns = []
for file in files:
    f = open(dir+file, 'rb')
    all_returns.append(pickle.load(f))
    f.close()

dir_wob = 'runs_data_cartpole1_50runs_new/testing/nobaseline/'
files_wob = os.listdir(dir_wob)
all_returns_wob = []
for file_wob in files_wob:
    f_wob = open(dir_wob+file_wob, 'rb')
    all_returns_wob.append(pickle.load(f_wob))
    f_wob.close()

dir_ppo = 'runs_data_cartpole1_50runs_new/testing/baseline_discounted/'
files_ppo = os.listdir(dir_ppo)
all_returns_ppo = []
for file_ppo in files_ppo:
    f_ppo = open(dir_ppo+file_ppo, 'rb')
    all_returns_ppo.append(pickle.load(f_ppo))
    f_ppo.close()

dir_ppo1 = 'runs_data_cartpole1_50runs_new/testing/nobaseline_discounted/'
files_ppo1 = os.listdir(dir_ppo1)
all_returns_ppo1 = []
for file_ppo1 in files_ppo1:
    f_ppo1 = open(dir_ppo1+file_ppo1, 'rb')
    all_returns_ppo1.append(pickle.load(f_ppo1))
    f_ppo1.close()



plt.figure(figsize=(12,8))
plt.title("Episodic Return")
plt.xlabel("Episode")
plt.ylabel("Average Return (Sliding Window 100)")
window = 100

runs = 50
episodes = [i for i in range(0,100)]
for i in range(1):
    sampled_results = []        
    for j in range(runs):
        sampled_results.append(np.array(all_returns[j]))
        #sampled_results.append(np.array(all_returns[random.randint(0,29)]))
    result_mean = []
    result_std = []
    for k in range(len(episodes)):
        samples = []
        for l in range(len(sampled_results)):
            samples.append(sampled_results[l][k])
        result_mean.append(np.mean(samples))
        result_std.append(np.std(samples))
    result_std = np.array(result_std)
    result_mean_p_std = result_mean + result_std
    result_mean_m_std = result_mean - result_std
    for k in range(len(result_mean_p_std)):
        if result_mean_p_std[k] >= 500:
            result_mean_p_std[k] = 500
        if result_mean_m_std[k] <= 0:
            result_mean_m_std[k] = 0
    plt.plot(episodes, sliding_window(list(result_mean), window), label='With baseline, undiscounted, averaged over 50 runs')
    plt.fill_between(episodes, sliding_window(list(result_mean_p_std), window), sliding_window(list(result_mean_m_std),window), alpha=0.25)

'''
runs = 50
episodes = [i for i in range(0,100)]
for i in range(1):
    sampled_results = []        
    for j in range(runs):
        sampled_results.append(np.array(all_returns_wob[j]))
        #sampled_results.append(np.array(all_returns[random.randint(0,29)]))
    result_mean = []
    result_std = []
    for k in range(len(episodes)):
        samples = []
        for l in range(len(sampled_results)):
            samples.append(sampled_results[l][k])
        result_mean.append(np.mean(samples))
        result_std.append(np.std(samples))
    result_std = np.array(result_std)
    result_mean_p_std = result_mean + result_std
    result_mean_m_std = result_mean - result_std
    for k in range(len(result_mean_p_std)):
        if result_mean_p_std[k] >= 500:
            result_mean_p_std[k] = 500
        if result_mean_m_std[k] <= 0:
            result_mean_m_std[k] = 0
    plt.plot(episodes, sliding_window(list(result_mean), window), label='Without baseline, undiscounted, averaged over 50 runs')
    plt.fill_between(episodes, sliding_window(list(result_mean_p_std), window), sliding_window(list(result_mean_m_std),window), alpha=0.25)
'''

runs = 50
episodes = [i for i in range(0,100)]
for i in range(1):
    sampled_results = []        
    for j in range(runs):
        sampled_results.append(np.array(all_returns_ppo[j]))
        #sampled_results.append(np.array(all_returns[random.randint(0,29)]))
    result_mean = []
    result_std = []
    for k in range(len(episodes)):
        samples = []
        for l in range(len(sampled_results)):
            samples.append(sampled_results[l][k])
        result_mean.append(np.mean(samples))
        result_std.append(np.std(samples))
    result_std = np.array(result_std)
    result_mean_p_std = result_mean + result_std
    result_mean_m_std = result_mean - result_std
    for k in range(len(result_mean_p_std)):
        if result_mean_p_std[k] >= 500:
            result_mean_p_std[k] = 500
        if result_mean_m_std[k] <= 0:
            result_mean_m_std[k] = 0
    plt.plot(episodes, sliding_window(list(result_mean), window),color='g',label='With baseline, discounted, averaged over 50 runs')
    plt.fill_between(episodes, sliding_window(list(result_mean_p_std), window), sliding_window(list(result_mean_m_std),window),color='g',alpha=0.25)

'''
runs = 50
episodes = [i for i in range(0,100)]
for i in range(1):
    sampled_results = []        
    for j in range(runs):
        sampled_results.append(np.array(all_returns_ppo1[j]))
        #sampled_results.append(np.array(all_returns[random.randint(0,29)]))
    result_mean = []
    result_std = []
    for k in range(len(episodes)):
        samples = []
        for l in range(len(sampled_results)):
            samples.append(sampled_results[l][k])
        result_mean.append(np.mean(samples))
        result_std.append(np.std(samples))
    result_std = np.array(result_std)
    result_mean_p_std = result_mean + result_std
    result_mean_m_std = result_mean - result_std
    for k in range(len(result_mean_p_std)):
        if result_mean_p_std[k] >= 500:
            result_mean_p_std[k] = 500
        if result_mean_m_std[k] <= 0:
            result_mean_m_std[k] = 0
    plt.plot(episodes, sliding_window(list(result_mean), window), label='Without baseline, discounted, averaged over 50 runs')
    plt.fill_between(episodes, sliding_window(list(result_mean_p_std), window), sliding_window(list(result_mean_m_std),window), alpha=0.25)
'''
plt.legend()
plt.show()

