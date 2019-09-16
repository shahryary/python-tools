#!/usr/bin/env python
#
# develop by Yadollah Shahryary (shahryary@gmail.com),
#
import h5py
import numpy as np

def format(data):

    if (data.dtype == '|S5') | (data.dtype == '|S1'):
        data = data.astype(np.int)
    if data.dtype == 'float64':
        csvfmt = '%.18e'
    elif data.dtype == 'int64':
        csvfmt = '%d'
    else:
        csvfmt = '%s'
    return(csvfmt,data)


def  hdf2Csv(filename, outdir):
    
    try:
        f = h5py.File(filename, 'r')
        a_dset_keys = list(f.keys())
        for dset in a_dset_keys:
            data = f[dset][()]
            if data.ndim == 0:
                val = data[()]
                data = np.array([val])

            print ('dataset=', dset)
            res = format(data)
            csvfmt = res[0]
            data = res[1]
            np.savetxt(outdir+'/out_val_'+ dset+ '.csv', data, fmt = csvfmt, delimiter = ',')

            #print attribute
            g = f[dset]
            if g.attrs.keys():
                listAtt = g.attrs.keys()
                for att in listAtt:
                    res = g.attrs[att]
                    if not isinstance(res, np.ndarray):
                        val=res
                        res=np.array([val])

                    res=format(res)
                    fmt = res[0]
                    da = res[1]
                    np.savetxt(outdir + '/out_attr_' + dset + "_" + att + '.csv', da, fmt=fmt, delimiter=',')

            print("Exported all the data-sets in: ", outdir)
    except Exception as e:
        #logging.error(traceback.format_exc())
        print(e.message)
