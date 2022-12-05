# In[] Modulo os
import os

cartella = (os.listdir())

for x in cartella:
    if os.path.isdir(x):
        print(f"DIR:{x}")
    elif os.path.isfile(x):
        print(f"FILE:{x}")

# In[]
import os
def browse_dir(d):
    
    cartella = (os.listdir(d))

    for x in cartella:
        if os.path.isfile(x):
            print(f"FILE:{x}")
        elif os.path.isdir(x):
            browse_dir(x)

browse_dir(os.getcwd())

# %% 