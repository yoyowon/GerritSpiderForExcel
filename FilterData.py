# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from pandas import DataFrame

def filder_project(e_path, pj_name, branch):
	e_data = pd.read_excel(e_path)
	ae_date = e_data[(e_data['project'].str.contains(pj_name)) & (e_data['branch'] == yfvet_public)]
	A = DataFrame(ae_date)
	A.to_excel(e_path, sheet_name='sheet1', index=False, header=True)