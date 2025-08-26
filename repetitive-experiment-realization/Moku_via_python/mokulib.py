import time
import numpy as np
import torch 
def osc_test_np(osc,channel = 'ch1',averaging = 1):
    time.sleep(0.02)
    data = []
    for i in range(averaging):
        data.append(osc.get_data(wait_complete= True)[channel])
    av = np.array(data)
    result = np.mean(av, 0)
    result = result.reshape(-1,1)
    return result
def osc_test_tensor(osc,channel = 'ch1',averaging = 1):
    time.sleep(0.02)
    data = []
    for i in range(averaging):
        data.append(osc.get_data(wait_complete= True)[channel])
    av = torch.tensor(data)
    result = torch.mean(av, 0)
    result = result.reshape(1,-1)
    return result
def fra_test_np(fra,channel = 'ch1',target = 'magnitude',averaging = 1):
    data = []
    for i in range(averaging):
        fra.start_sweep()
        data.append(fra.get_data(wait_complete=True)[channel][target])
        fra.stop_sweep()
    av = np.array(data)
    result = np.mean(av,0).reshape(-1,1)
    return result