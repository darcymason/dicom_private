
"""Collect vendor tags used across multiple private creator names from that vendor"""

from collections import defaultdict
from dicom_private.compare_priv import tag_creator_dict
from dicom_private.dicts.dcmtk import dcmtk_dict
from dicom_private.dicts.dicom3tools import dicom3tools_dict
from dicom_private.dicts.gdcm import gdcm_dict
from dicom_private.dicts.tcia import tcia_dict
from dicom_private.dicts.dcm2nii import dcm2nii_dict
    


if __name__ == "__main__":
    source_dicts = (dcmtk_dict, dicom3tools_dict, gdcm_dict, tcia_dict)
    source_names = ["DCMTK", "dicom3tools", "GDCM", "TCIA"]

    inverted = tag_creator_dict(dcmtk_dict)
    
    # Take the inverstion further and combine creators into a vendor
    vendors = ["siemens"]
    compressed = defaultdict(lambda: defaultdict(list))
    for vendor in vendors:
        for tag, creator_vals_dict in inverted.items():
            for creator, vals in creator_vals_dict.items():
                if creator.lower().startswith(vendor):
                    compressed[vendor][tag].append((creator, *vals))
    
    print("Vendors with same tag re-used")
    for vendor, tag_dict in compressed.items():
        print(f"Vendor: {vendor}")
        for tag, vals_list in tag_dict.items(): 
            if len(vals_list) > 1:
                print(tag)
                print("\n".join(str(x) for x in vals_list))

