# Week 3 exercises - Markov Chains

import numpy as np

# 2
P1 = np.matrix([[0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
                [1, 0, 0, 0]
                ])
P2 = np.matrix([[0, 0.5, 0, 0.5, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0.5, 0, 0.5],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0]
                ])
# for i in np.arange(1, 10):
#     print('P1**{} = \n{}'.format(i, P1**i))
print(P1**50)

for i in np.arange(50, 100, step=5):
    print('P2**{} = \n{}'.format(i, P2**i))

# 3
P = np.matrix([[1/3, 1/3, 1/3, 0],
               [1/2, 1/2, 0, 0],
               [1/4, 1/4, 0, 1/2],
               [0, 1/2, 0, 1/2]
               ])
for i in np.arange(1, 20):
    print('P**{} = \n{}'.format(i, P**i))


