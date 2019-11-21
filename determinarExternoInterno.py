import json
import numpy as np
from matplotlib.path import Path

dado = json.load(open('geometry.epJSON', 'r'))

cg = dado['Wire001']['centroZona']
walls = dado['Wire001']['paredes']

cg = np.array(cg)[:-1]
walls = np.array(walls)
walls.shape

path = Path(np.vstack(walls))
path.contains_point(cg)

wall = walls[4]
cgw = np.mean(wall, axis=1)
cgw0 = cgw+1
cgw1 = cgw-1

path.contains_point(cgw0)
path.contains_point(cgw1)

cgw
