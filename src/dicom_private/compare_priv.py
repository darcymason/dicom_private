# compare_priv.py
"""Gather various private dicts and output files for easy diff
"""
from collections import defaultdict


def compare(source_dicts):
    """Collapse private dicts into something like:
        creator/tag -> list(each source's result or None),
        e.g.
        {
           'CREATOR_1' : {
                '0029xx00': [(vr1, vm1, name1, '') or None, (vr2, vm2, name2, '') or None, ...],
                ...
            },
            ...
        }
    """
    union = defaultdict(dict)
    all_creators = sorted(set().union(*[di.keys() for di in source_dicts]))
    for creator in all_creators:
        all_tags = sorted(
            set().union(
                *[di[creator].keys() for di in source_dicts if creator in di]
            )
        )
        for tag in all_tags:
            entry_list = []
            for source in source_dicts:
                try:
                    val = source[creator][tag]                
                except KeyError:
                    val = None
                entry_list.append(val)
            union[creator][tag] = entry_list
    return union
       

if __name__ == "__main__":
    from dicom_private.dicts.dcmtk import dcmtk_dict
    from dicom_private.dicts.gdcm import gdcm_dict
    from dicom_private.dicts.tcia import tcia_dict

    source_dicts = (dcmtk_dict, gdcm_dict, tcia_dict)
    descriptions = ["DCMTK", "GDCM", "TCIA"]

    union_dict = compare(source_dicts)
    print(union_dict)