# compare_priv.py
"""Gather various private dicts and output files for easy diff
"""
from collections import defaultdict
import difflib
import itertools
from dicom_private.core import REPORT_PATH
from dicom_private.compare_priv import UNKNOWNS, make_union_dict

VR, VM, NAME = range(3)  # index into dict results


def make_keyword(s):
    s = s.replace(" ", "").replace("_", "")
    return s

def non_similars(source_dicts, threshold_ratio=0.6):
    """Return creator/tag comparisons where sources are dissimilar"""
   
    # Get union (creator -> tag -> list of values for each source, or None)
    union = make_union_dict(source_dicts)
    for creator, tag_dict in union.items():
        for tag, source_vals in tag_dict.items():
            names = [
                source_val[NAME] if source_val else ''
                for source_val in source_vals
            ]
            sanitized_names = [
                make_keyword(name).lower()
                for name in names
                if name and name.lower() not in UNKNOWNS
            ]
            if len(sanitized_names) < 2:
                continue
            if any(
                difflib.SequenceMatcher(None, name1, name2).ratio() < threshold_ratio
                and name1 not in name2 and name2 not in name1
                for name1, name2 in itertools.combinations(sanitized_names, 2)
            ):
                yield  (creator, tag, *names)
    # for creator in all_creators:
    #     tag_dict1 = source1[creator]
    #     tag_dict2 = source2[creator]
    #     tags = set(tag_dict1.keys()).intersection(tag_dict2.keys())
    #     for tag in tags:
    #         name1 = tag_dict1[tag][NAME]
    #         name2 = tag_dict2[tag][NAME]
    #         name1_sanitized = make_keyword(name1).lower()
    #         name2_sanitized = make_keyword(name2).lower()
    #         if name1.lower() in UNKNOWNS or name2.lower() in UNKNOWNS:
    #             continue
    #         seq_matcher = difflib.SequenceMatcher(None, name1_sanitized, name2_sanitized)
    #         if seq_matcher.ratio() < threshold_ratio:
    #             if name1_sanitized not in name2_sanitized and name2_sanitized not in name1_sanitized:
    #                 yield  (creator, tag, name1, name2)


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
    print("|--|--|" + "--|" * len(source_names))

    for diff in non_similars(compare_sources):
        print(f"|{'|'.join(diff)}|")
    # main_file = REPORT_PATH / "non-similar.html"
    # print(f"Write {main_file}")
    # with open(main_file, "w", encoding="utf-8") as f:
    #     f.write(html)
    # print(f"Write {unknowns_file}")
    # with open(unknowns_file, "w", encoding="utf-8") as f:
    #     f.write(unknowns)
