#!/usr/bin/env python
#
# develop by Yadollah Shahryary (shahryary@gmail.com),
#
import h5py
import numpy as np

def  hdfTocsv(filename, outdir):
    
    try:
        h5f = h5py.File(filename, 'r')
        a_dset_keys = list(h5f.keys())

        for dset in a_dset_keys :
            data = h5f[dset][()]
            if data.ndim == 0 :
                val = data[()]
                data = np.array([val])

            print ('dataset=', dset)
            
            if data.dtype == '|S5':
                data=data.astype(np.int)
            if data.dtype == 'float64' :
                csvfmt = '%.18e'
            elif data.dtype == 'int64' :
                csvfmt = '%d'
            else:
                csvfmt = '%s'

            np.savetxt(outdir+'/output_'+ dset+ '.csv', data, fmt = csvfmt, delimiter = ',')
            print("Exported all the data-sets in: ", outdir)
    except Exception as e:
        #logging.error(traceback.format_exc())
        print(e.message)