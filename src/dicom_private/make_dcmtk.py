# Copyright (c) 2025 Darcy Mason and contributors. All rights reserved.
# See LICENSE file for details
"""Generate a private dict file fomr dcmtk private tags file 
(https://github.com/InsightSoftwareConsortium/DCMTK/blob/master/dcmdata/data/private.dic)

"""
from collections import defaultdict, namedtuple
import csv
from datetime import datetime
import re
from typing import Generator
from urllib.request import urlopen

from dicom_private.core import write_dict


DCMTK_URL = (
    "https://raw.githubusercontent.com/InsightSoftwareConsortium/DCMTK/"
    "refs/heads/master/dcmdata/data/private.dic"
)
DCMTK_FIELDS = "creator tag vr name vm".split()
DcmtkLine = namedtuple("DcmtkLine", DCMTK_FIELDS)
DICT_FILENAME = "dcmtk.py"
PY_NAME = "dcmtk_dict"
DICT_DOCSTRING = f"""DICOM private dictionary auto-generated by make_dcmtk.py.

Data generated {datetime.now():%Y-%m-%d %H:%M} from
{DCMTK_URL}

The outer dictionary key is the Private Creator name ("owner"), while the inner
dictionary key is a map of DICOM tag to (VR, VM, name, is_retired).
"""


# (gggg,"CREATOR",ee)
# (gggg,"CREATOR",eeee) [eeee >= 1000]
# (gggg-o-gggg,"CREATOR",ee) or (gggg-o-gggg,"CREATOR",eeee)
# where "-o-" indicates that only odd group numbers match the definition.
RE_TAG_CREATOR_PATTERN = re.compile(
    r"\((.*?)"  # tag as in comments above
    r',"(.*?)"'  # Creator
    r",(.*?)\)"  # Final 2 or 4-digit hex tag element
)
RE_REPEATER_TAG_PATTERN = re.compile(
    r"(.*?)-O-(.*?)"
)  # tag is capitalized before match so cap 'O'


def parse_tag_creator(elem: str) -> tuple[str, str]:
    match = RE_TAG_CREATOR_PATTERN.match(elem)
    if not match:
        raise ValueError(f"Unable to parse tag/creator pattern '{elem}'")
    tag1, creator, tag2 = match.groups()
    tag1 = tag1.upper()

    # Check repeater tag
    # Every one in the file currently is like 'ee01-o-eeFF',
    # so currently only need first two chrs
    if RE_REPEATER_TAG_PATTERN.match(tag1):
        tag1 = f"{tag1[:2]}xx"

    tag2 = tag2.upper()
    if len(tag2) == 2:
        tag2 = f"xx{tag2}"
    return (creator, f"{tag1}{tag2}")


def DCMTK_reader(reader) -> Generator[tuple[str, str, str, str, str, str], None, None]:
    """Return parsed lines, each a named tuple (DcmtkLine)"""

    csv_reader = csv.DictReader(
        (row for row in reader if row and not row.startswith("#")),
        fieldnames="tag_creator vr name vm tag_type".split(),
        delimiter="\t",
    )

    # "tag creator vr name vm tag_type"
    for row in csv_reader:
        creator, tag = parse_tag_creator(row["tag_creator"])
        yield DcmtkLine(creator, tag, row["vr"], row["name"], row["vm"])


def private_dictionaries(reader) -> dict[str, dict[str, tuple[str, str, str, str]]]:
    """Reformat original data into kind needed for pydicom-style dict
    Params:
    reader: file-like
        Object that iterates one original dict line at a time
    """
    dicts = defaultdict(dict)
    for line in DCMTK_reader(reader):
        dicts[line.creator][line.tag] = (line.vr, line.vm, line.name)

    return dicts


if __name__ == "__main__":

    with urlopen(DCMTK_URL) as response:
        reader = response.read().decode("utf-8").splitlines()
        priv_dict = private_dictionaries(reader)

    write_dict(priv_dict, DICT_FILENAME, docstring=DICT_DOCSTRING, py_name=PY_NAME)
