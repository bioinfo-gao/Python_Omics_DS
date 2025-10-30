# Index
# (Preface)  ==> Line12 == startup
# (A) ==> Line 10 == Jupyter Lab
# (A.A) ==> Line 10 == fast key
# (A.B) ==> Line 110 == run kernel or get help
# (A.C) ==> Line 130 == install package 
# (A.D) ==> Line 140 == list module in a library e 
# (1.4) ==> Line 150 == run python command or code 
# (2) ==> Line 120 == Markdown
# (3) ==> Line 10 == Termnial
# (3) ==> Line 150 == Python console

#  =====(Preface)===== 
#  =====(Pre1)===== START UP 
# in windows powershell or linux terminal
jupyter notebook
jupyter labk

#  =====(Pre1)===== Switch       to jupyterLab from Jupyter notebook 
# just input in address line
http://localhost:8888/lab

# =====(A) general short keyboard shortcuts
=====(0)=== This menu can be found in Help > Show Keyboard Shortcuts in any open notebook.

# =====(AA)=====  duplicate a line
# =====(AA1)=====  duplicate a line to next line
shift + alt  + down for duplicate a line

# =====(AA2)==== # select a block of line down
shift + down to the final line  #  =====(1.2)==== # duplicate a line or a block down # shift + ctrl + down

# =====(AA3)===== duploicate cell 
for each cell, there is a [+] for dulicate this cell

# =====(AA4)===== # comment out mulitple lines    ### remove comment same command
Ctrl + /      

# =====(AA5)===== # sholw line number 
View ==> Show line Number

# =====(AA6)===== # delete a line 
=====(3A)===== # delete a line                    # or Ctrl + D or both, depending on version
Shift + Delete-Key
=====(3B)===== # delete a world after the current position 
Ctl + Delete-Key
=====(3B)===== # delete a world before the current position
Ctl + Backspace 

# =====(AA7)===== # check all resource path
http://localhost:8888/lab/workspaces/auto-p/tree/Documents/Jupyter_DeepL >  jupyter --paths
config:
    C:\Users\zhen-\.jupyter
    C:\Users\zhen-\AppData\Roaming\Python\etc\jupyter
    C:\Users\zhen-\Anaconda3\etc\jupyter
    C:\ProgramData\jupyter
data:
    C:\Users\zhen-\AppData\Roaming\jupyter
    C:\Users\zhen-\AppData\Roaming\Python\share\jupyter
    C:\Users\zhen-\Anaconda3\share\jupyter
    C:\ProgramData\jupyter
runtime:
    C:\Users\zhen-\AppData\Roaming\jupyter\runtime

# =====(AA8)===== # check all resource path  =====
(base) PS C:\Users\zhen->   jupyter kernelspec list
Available kernels:
  python3    C:\Users\zhen-\Anaconda3\share\jupyter\kernels\python3
  Ir         C:\Users\zhen-\Anaconda3\share\jupyter\kernels\ir

  

# =====(4)===== delete output 
=======> Change the cell type to raw then back to code: For versions less than 5: Option 1 -- quick hack:
#实际上不work Option 2 quick hack: https://www.geeksforgeeks.org/keyboard-shortcuts-to-clear-cell-output-in-jupyter-notebook/  EscRY will discard the output.

# =====(5)===== for pair symbol
shift + ( automatic and another piece of pair
shift + "

# =====(6)===== copy to another file
# copy a cell from one jupyter notebook to another?
Ctrl-C and Ctrl-V (Cmd-C and Cmd-V on Mac).

# =====(7)=====  # move a line down

# =====(8)===== collaps mutilple cells In the jupyterLab 
JupyterLab supports cell collapsing. 
Clicking on the blue cell bar on the left will fold the cell.just input
ctrl + down

# =====(9)===== clear output In the jupyterLab 
JupyterLab supports cell collapsing. 
Clicking on the top edit ==> clear cell output blue

# =====(10)===== clear output In the jupyterLab 
JupyterLab  
right Clicking, select end==? select the "variable inspector" see all vaiavble structure

# =====(11)====================================================================== cmd for runn code 
ctl + enter   # run the current line and keep in this line
shift + enter # run the current line and goto next line

# =====(12)===== cmd for several cell 
Note on multiple cells: currently (jupyter 6.0.0) on Mac+chrome using shift-click to select the cells then cmd-C does NOT work, while using the keyboard with shift-down-arrow does! (thanks drevicko for pointing this out)

# =====(B)=============== get help or list funtions
# import numpy              as np
# =====(B1)======================================================== get help
help(np.linspace)  get help for a function 

# =====(B2)=============== list all function after 
dir(np) #dir(numpy)   

# =====(B3)=============== find which module a function comes from? 
# https://stackoverflow.com/questions/54499198/how-do-i-tell-which-module-a-function-comes-from  
import inspect
print(inspect.getfile(update_parameters_with_gd_test_case))

# =====(B4)===== running and kernel
if stuck with * (contantly runing), Just go to kernel ==> restart kernel

# ======(C) install package ================================================== chapter 4
# ======(C1)==== install package ================================================== chapter 4
# https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/
# Install a conda package in the current Jupyter kernel
# ZG Note : this is is Perfect!!
import sys
!{sys.executable} -m pip install PyGame 
!{sys.executable} -m pip install PyOpenGL 

in Terminal
pip install -U scikit-learn
conda install -c conda-forge scikit-learn


# ======(D) list moudle in package ================================================== chapter 4
# ======(C1)==== list =============================== chapter 4
# list all modules in a library
import os.path, pkgutil
import pandas
pkgpath = os.path.dirname(pandas.__file__)
print([name for _, name, _ in pkgutil.iter_modules([pkgpath])])



# =====(C2)===== run python
# run python command
!pip list

========== note
========== note
draw3D of math of develpers works good =======> Chapter 5 Walkthrough.ipynb
critical image work =======> ch06_walkthrough

======(D) Markdown 
====(1A)=========== color 
<font color='blue'>
as a beging line 
====(1B)=========== color 
<span style="color:red"> $$a^{[1] (i)} = \tanh(z^{[1] (i)}) \tag{2} $$  </span> 
====(2)=========== bold , italic and two formats 
https://www.markdownguide.org/basic-syntax/#:~:text=To%20bold%20text%2C%20add%20two,without%20spaces%20around%20the%20letters.&text=I%20just%20love%20**bold%20text**.

======================== color list ================================https://www.memphis.edu/webdev/html/html-colors.php
aqua - <span style="color:aqua">aqua</span>
black - <span style="color:black">black</span>
blue - <span style="color:blue">blue</span>
fuchsia - <span style="color:fuchsia">fuchsia</span>
gray - <span style="color:gray">gray</span>
green - <span style="color:green">green</span>
lime - <span style="color:lime">lime</span>
maroon - <span style="color:maroon">maroon</span>
navy - <span style="color:navy">navy</span>
olive - <span style="color:olive">olive</span>
purple - <span style="color:purple">purple</span>
red - <span style="color:red">red</span>
silver - <span style="color:silver">silver</span>
teal - <span style="color:teal">teal</span>
white - <span style="color:white">white</span>
yellow - <span style="color:yellow">yellow</span>
pink
======================== color list ================================

======================== console ================================
import os
os.system('cls')