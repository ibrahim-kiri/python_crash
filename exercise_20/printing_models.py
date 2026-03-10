import printing_functions

unprinted_designs = ['phone', 'robot', 'doll']
completed_models = []
printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)

from printing_functions import print_models

unprinted_designs = ['book', 'bottle', 'pen']
completed_models = []
print_models(unprinted_designs, completed_models)

from printing_functions import show_completed_models as scm

unprinted_designs = ['rubber', 'charger', 'razar']
completed_models = []
print_models(unprinted_designs, completed_models)
scm(completed_models)

import printing_functions as pf

unprinted_designs = ['mat', 'curtain', 'bag']
completed_models = []
pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)

from printing_functions import *

unprinted_designs = ['iron', 'laptop', 'cup']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
