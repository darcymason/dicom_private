# compare_priv.py
"""Gather various private dicts and output files for easy diff
"""
from collections import defaultdict
import difflib
from dicom_private.core import REPORT_PATH
from dicom_private.compare_priv import UNKNOWNS

VR, VM, NAME = range(3)  # index into dict results


def make_keyword(s):
    s = s.replace(" ", "").replace("_", "")
    return s

def non_similars(source_dicts, threshold_ratio=0.6):
    """Return creator/tag comparisons where sources are dissimilar"""
    assert len(source_dicts) == 2, "Can only find non-similar from two sources"
    source1, source2 = source_dicts
    creators = set(source1.keys()).intersection(source2.keys())
    for creator in creators:
        tag_dict1 = source1[creator]
        tag_dict2 = source2[creator]
        tags = set(tag_dict1.keys()).intersection(tag_dict2.keys())
        for tag in tags:
            name1 = tag_dict1[tag][NAME]
            name2 = tag_dict2[tag][NAME]
            name1_sanitized = make_keyword(name1).lower()
            name2_sanitized = make_keyword(name2).lower()
            if name1.lower() in UNKNOWNS or name2.lower() in UNKNOWNS:
                continue
            seq_matcher = difflib.SequenceMatcher(None, name1_sanitized, name2_sanitized)
            if seq_matcher.ratio() < threshold_ratio:
                if name1_sanitized not in name2_sanitized and name2_sanitized not in name1_sanitized:
                    yield  (creator, tag, name1, name2)


if __name__ == "__main__":
    from dicom_private.dicts.dcmtk import dcmtk_dict
    from dicom_private.dicts.dicom3tools import dicom3tools_dict
    from dicom_private.dicts.gdcm import gdcm_dict
    from dicom_private.dicts.tcia import tcia_dict
    from dicom_private.dicts.DICOM_safe import safe_private_dict


    compare_sources = (dicom3tools_dict, gdcm_dict)
    source_names = ["dicom3tools", "GDCM"]

    # Output as markdown table:
    print(f"|Creator|Tag|{'|'.join(source_names)}|")
    print("|--|--|--|--|")

    for diff in non_similars(compare_sources):
        print(f"|{'|'.join(diff)}|")
    # main_file = REPORT_PATH / "non-similar.html"
    # print(f"Write {main_file}")
    # with open(main_file, "w", encoding="utf-8") as f:
    #     f.write(html)
    # print(f"Write {unknowns_file}")
    # with open(unknowns_file, "w", encoding="utf-8") as f:
    #     f.write(unknowns)
