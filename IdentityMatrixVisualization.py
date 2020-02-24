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
                    identity = [float(i) for i in line[2:]]
                    SeqNames.append(line[1])
                    if flag == 0:
                        seqID = identity
                        flag = 1
                    else:
                        seqID = np.vstack((seqID, identity))

    print(np.amin(seqID))
    print(np.amax(seqID))

    ClustalSeqID = pd.DataFrame(data=seqID, index=SeqNames, columns=SeqNames)

    return ClustalSeqID

def PlotClustalMatrix(ClustalMatrix):
    """
    Plot the Clustal MAtrix as an heatmap
    :param ClustalMatrix: matrix from ReadClustalMatrix function
    :return: PLot the heatmap
    """

    fig, ax = plt.subplots()
    plt.rcParams["xtick.labelsize"] = 14
    plt.rcParams["ytick.labelsize"] = 14
    plt.rcParams["axes.labelsize"] = 16
    plt.rcParams["axes.labelsize"] = 16

    fig, ax = plt.subplots(1, 1,figsize=(25, 10), sharex='col', sharey='row', gridspec_kw={'hspace': 0, 'wspace': 0})

    plt.imshow(ClustalMatrix, cmap="YlGnBu")
    cbar = plt.colorbar()
    cbar.set_label('Sequence Identity (%)')


    plt.xticks(range(len(ClustalMatrix)),ClustalMatrix.columns,rotation=80)
    plt.yticks(range(len(ClustalMatrix)),ClustalMatrix.index)



    plt.savefig("ClustalIDMatrix.png", dpi=150, papertype="a4", orientation="portrait", format="tiff",bbox_inches = 'tight')


if __name__ == '__main__':

    ClustalMatrix =ReadClustalMatrix(sys.argv[1])
    PlotClustalMatrix(ClustalMatrix)