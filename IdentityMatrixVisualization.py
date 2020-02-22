#!/usr/bin/env python
# ~*~ coding:utf-8 ~*~

__author__ = "Emmanuel Edouard MOUTOUSSAMY"
__version__  = "1.0.0"
__copyright__ = "copyleft"
__date__ = "2020/02"

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def ReadClustalMatrix(ClustalOutput):
    """
    Read ClustalOmega output (Percent Identity Matrix)
    :param ClustalOutput:Percent Identity Matrix from ClustalOmega
    :return: a panda matrix
    """

    SeqNames = []
    flag = 0
    with open(ClustalOutput) as ClustalInfos:
        for line in ClustalInfos:
            if "#" not in line:
                line = line.split()
                if line != []:
                    SeqNames.append(line[1])
                    if flag == 0:
                        seqID = line[2:]
                        flag = 1
                    else:
                        seqID = np.vstack((seqID, line[2:]))

    ClustalSeqID = pd.DataFrame(data=seqID, index=SeqNames, columns=SeqNames)

    return ClustalSeqID

if __name__ == '__main__':
    ReadClustalMatrix(sys.argv[1])