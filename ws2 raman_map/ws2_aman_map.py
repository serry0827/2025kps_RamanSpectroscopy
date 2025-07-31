import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

for i in range(0,4):
    df = pd.read_csv(r"C:\Users\serry\Documents\GitHub\2025kps_RamanSpectroscopy\experimental data\ws2 raman_map.CSV", skiprows=41)
    data = df.pivot_table(index="Y", columns="X", values=f"CHNO={i}", aggfunc="mean")
    data = data.iloc[::-1]
    
    fig, ax = plt.subplots()
    im = ax.imshow(data, cmap="magma", interpolation="bilinear", origin="lower")  
    ax.axis('off')

    cbar = fig.colorbar(im, ax=ax)
    cbar.ax.tick_params(length=0)
    cbar.set_label("Intensity")

    filename = fr"C:\Users\serry\Documents\GitHub\2025kps_RamanSpectroscopy\ws2 raman_map\CHNO{i}.png"
    fig.savefig(filename, dpi=300, bbox_inches="tight")
    plt.close(fig)

    #data = df.pivot_table(index="Y", columns="X", values="CHNO=0", aggfunc="mean")
    #hm = sns.heatmap(data=data, annot=False, xticklabels=False, yticklabels=False)
    #hm.set_xticklabels([])
    #hm.set_yticklabels([])
    #plt.show()