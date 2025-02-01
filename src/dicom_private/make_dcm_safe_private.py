# Copyright (c) 2025 Darcy Mason and contributors. All rights reserved.
# See LICENSE file for details
"""Create a pydicom-style private dict with the information in the DICOM safe private table"""
from datetime import datetime
import re
import xml.etree.ElementTree as ET
from urllib.request import urlopen
from collections import defaultdict

from pydicom.valuerep import VR
from dicom_private.core import DICTS_PATH, write_dict
from collections import namedtuple


DICOM_SAFE_PRIVATE_URL = (
    r"https://dicom.nema.org/medical/dicom/current/output/html/part15.html"
)
fields = "tag creator vr vm meaning".split()
Entry = namedtuple("Entry", fields)
RE_TAG_PATTERN = re.compile(
    r"\(([0-9A-Fa-f]{4}),([x0-9A-Fa-f]{4})\)"
)
PY_NAME = "safe_private_dict"
DICT_FILENAME = "DICOM_safe.py"
DICT_DOCSTRING = f"""DICOM private dictionary auto-generated by make_dcm_safe_private.py.

Data generated {datetime.now():%Y-%m-%d %H:%M} from
{DICOM_SAFE_PRIVATE_URL}

The outer dictionary key is the Private Creator name ("owner"), while the inner
dictionary key is a map of DICOM tag to (VR, VM, name, is_retired).
"""



def entry_reader(xml_text):
    root = ET.fromstring(xml_text)

    namespaces = {
        "ns": "http://docbook.org/ns/docbook",
        "xml": "http://www.w3.org/XML/1998/namespace",
        "xhtml": "http://www.w3.org/1999/xhtml",
        "xl": "http://www.w3.org/1999/xlink",
    }

    tbl = root.find(
        ".//ns:section[@xml:id='sect_E.3.10']"
        "//ns:table[@xml:id='table_E.3.10-1']",
        namespaces=namespaces
    )
    
    td_paras = tbl.findall(".//ns:para", namespaces=namespaces)
    for i in range(5, len(td_paras), 5):  # one row at a time; skip header
        yield Entry(*(e.text for e in td_paras[i:i+5]))

def private_dictionaries(xml_text):
    priv_dict = defaultdict(dict)
    for entry in entry_reader(xml_text):
        match = RE_TAG_PATTERN.match(entry.tag)
        if not match:
            raise ValueError(f"Unable to parse tag `{entry.tag}`")
        tag = "".join(match.groups()).upper().replace("XX", "xx")
        priv_dict[entry.creator][tag] = (entry.vr, entry.vm, entry.meaning or "")
    return priv_dict


if __name__ == "__main__":
    fn = r"g:\My drive\manuals\dicom\part15.xml"
    with open(fn, "r", encoding="utf-8") as f:
        text = f.read()
    # with urlopen(DICOM_SAFE_PRIVATE_URL) as response:
    #     text = response.read().decode("utf-8")

    priv_dict = private_dictionaries(text)
    write_dict(priv_dict, DICT_FILENAME, docstring=DICT_DOCSTRING, py_name=PY_NAME)
