# https://stackoverflow.com/questions/26494747/simple-way-to-choose-which-cells-to-run-in-ipython-notebook-during-run-all/43584169#43584169

# Load the extension in your notebook: -
# 
# %load_ext skip_kernel_extension
#
# -- or --
#
# %reload_ext skip_kernel_extension
# 
# Run the skip magic command in the cells you want to skip:
# 
# %%skip True  #skips cell
# %%skip False #won't skip
# 
# You can use a variable to decide if a cell should be skipped by using $:
# 
# should_skip = True
# %%skip $should_skip
# 

def skip(line, cell=None):
    '''Skips execution of the current line/cell if line evaluates to True.'''
    if eval(line):
        return

    get_ipython().ex(cell)

def load_ipython_extension(shell):
    '''Registers the skip magic when the extension loads.'''
    shell.register_magic_function(skip, 'line_cell')

def unload_ipython_extension(shell):
    '''Unregisters the skip magic when the extension unloads.'''
    del shell.magics_manager.magics['cell']['skip']
