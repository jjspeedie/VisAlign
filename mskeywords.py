import sys
import os
import numpy as np

import pyralysis
import pyralysis.io


def pointing(file_ms):

    reader = pyralysis.io.DaskMS(input_name=file_ms)
    dataset = reader.read(calculate_psf=False)
    print(">> pyralysis.io.DaskMS.read: Done reading "+file_ms)

    field_dataset = dataset.field.dataset
    # ref_dir = field_dataset[0].REFERENCE_DIR.compute()
    # phase_dir = field_dataset[0].PHASE_DIR.compute()
    # ref_dirs = []
    # phase_dirs = []
    #for i, row in enumerate(field_dataset):
    ref_dir = (180. / np.pi) * field_dataset.REFERENCE_DIR.compute().to_numpy()
    #ref_dir = np.squeeze(ref_dir)
    #print("ref_dir",ref_dir)
    ref_mask = ref_dir[:,:,0] < 0
    # if (ref_dir[:,0] < 0):

    ref_dir[ref_mask,0] += 360.

    phase_dir = (180. / np.pi) * field_dataset.PHASE_DIR.compute().to_numpy()
    #phase_dir = np.squeeze(phase_dir)
    phase_mask = phase_dir[:,:,0] < 0
    #if (phase_dir[:,0] < 0.):
    phase_dir[ref_mask,0] += 360.

    #ref_dirs.append(ref_dir)
    #phase_dirs.append(phase_dir)

    print(">> mskeywords.pointing: Reference direction = ", ref_dir)
    print(">> mskeywords.pointing: Phase direction = ", phase_dir)
    return ref_dir, phase_dir
