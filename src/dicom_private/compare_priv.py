# compare_priv.py
"""Gather various private dicts and output files for easy diff
"""
from collections import defaultdict
import difflib
import itertools
from dicom_private.core import REPORT_PATH
from html import escape
from urllib.parse import quote

VR, VM, NAME = range(3)  # index into dict results
UNKNOWNS = (
    "unknown",
    "<internal",
    "internal data",
    "&lt;internal",
    "",
    "internalvalue",
)

HTML_DOC_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<style>
.container {{
  display: grid;
  grid-template-columns: repeat({num_cols}, auto);
  padding: 10px;
  padding-top: 0px;
}}

.container > div {{
  background-color: #f8f8f8;
  border: 1px solid black;
  padding: 5px;
  text-align: left;
}}

/* Alternating rows */
{alt_rows_css_def} {{
  background-color: #e8f1f1;
}}

/* Header for each table */
.container > div:nth-child(-n + {num_cols}) {{ background-color: #d1d1d1; }}

/* Color markup for diffs */
.diff_add {{background-color:#aaffaa}}
.diff_chg {{background-color:#ffff77; word-wrap: break-word;}}
.diff_sub {{background-color:#ffcccc; word-wrap: break-word;text-decoration:line-through;}}

</style>
</head>
<body>

<main id="scroll-element">
{content}
</main>
</body>
</html>
"""


def make_keyword(s):
    s = s.replace(" ", "").replace("_", "")
    return s


def is_unknown(name):
    name = make_keyword(name).lower()
    return name.startswith("?") or "privatedata" in name or name in UNKNOWNS


def make_union_dict(source_dicts):
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

    i.e. creator -> tag - > list of results from the source dicts
    """
    union = defaultdict(dict)
    all_creators = sorted(set().union(*[di.keys() for di in source_dicts]))
    for creator in all_creators:
        all_tags = sorted(
            set().union(*[di[creator].keys() for di in source_dicts if creator in di])
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


def non_empty_creators(union_dict):
    non_empty = []
    for creator, tagdict in union_dict.items():
        if any(
            source_entry and not is_unknown(source_entry[NAME])
            for (tag, source_entries) in tagdict.items()
            for source_entry in source_entries
        ):
            non_empty.append(creator)
    return non_empty


red = lambda text: f'<span class="diff_sub">{text}</span>'
green = lambda text: f'<span class="diff_add">{text}</span>'
yellow = lambda text: f'<span class="diff_chg">{text}</span>'


def diff_new(old, new):
    codes = difflib.SequenceMatcher(a=old, b=new).get_opcodes()
    new2 = ""
    had_del = False
    if is_unknown(new):
        return new
    for code in codes:
        op = code[0]
        if op == "equal":
            new2 += new[code[3] : code[4]]
        elif op == "delete":
            new2 += red(old[code[1] : code[2]])
            had_del = True
        elif op == "insert":
            new2 += green(new[code[3] : code[4]])
        elif op == "replace":
            new2 += yellow(new[code[3] : code[4]])
    return new2 + (f"--> ({new})" if had_del else "")


def make_creator_compare_table(tag_dict, source_names):
    """Return one (text-only) 2D table of the compared sources and a list of which 'contributed'
    First table row is "Tag", then names of sources.
    Table row is simple list [tag, source1 name or keyword, source2 name or keyword, ...]
    """

    rows = [("Tag", *source_names)]
    for tag, entries in tag_dict.items():
        rows.append([tag] + [escape(entry[NAME]) if entry else "" for entry in entries])

    # Determine who contributed by columns non-empty (after header)
    # Transpose with zip(*)
    tr = zip(*rows[1:])
    col_non_empty = [
        any([e and (not is_unknown(e)) for e in col]) for col in tr
    ]
    contributed = itertools.compress(source_names, col_non_empty[1:])  # 1: for tag col
    return rows, list(contributed)


def html_compare(source_dicts, source_names):
    """Return two string representing HTML for non-empty and empty creators"""
    union_dict = make_union_dict(source_dicts)
    creators_non_empty = non_empty_creators(union_dict)

    header = "<div>Tag</div>" + "".join(f"<div>{descr}</div>" for descr in source_names)
    main_content = []
    unknown_content = []
    for creator, tag_dict in union_dict.items():
        content = main_content
        if creator not in creators_non_empty:
            main_content.append(
                f'<h1>{escape(creator)}: <a href="unknowns.html#{quote(creator)}">All unknown</a></h1>'
            )
            content = unknown_content  # for rest of this loop
        content.append(f'<h1 id="{quote(creator)}">{escape(creator)}</h1>')
        content.append('<div class="container">')
        content.append(header)
        for tag, vals in tag_dict.items():
            str_vals = [escape(val[NAME]) if val else "" for val in vals]
            non_empty = [s for s in str_vals if s and not is_unknown(s)]
            if non_empty:
                if len(non_empty) == 1:
                    div_vals = [
                        f"<div>{green(s) if s==non_empty[0] else s}</div>"
                        for s in str_vals
                    ]
                else:
                    div_vals = [
                        f"<div>{diff_new(non_empty[0], s) if s else ""}</div>"
                        for s in str_vals
                    ]
            else:  # could include 'Unknown's
                div_vals = [f"<div>{s}</div>" for s in str_vals]
            content.append(f"<div>{tag}</div>\n{"\n".join(div_vals)}")
        content.append("</div>")  # end of container
    main_content = "\n".join(main_content)
    unknown_content = "\n".join(unknown_content)
    num_cols = len(source_dicts) + 1
    # Can't get nth-child range to work so just list each one
    alt_rows_css_def = ",\n".join(
        f".container > div:nth-child({2*num_cols}n+{i})" for i in range(1, num_cols + 1)
    )

    html_main = HTML_DOC_TEMPLATE.format(
        num_cols=num_cols, content=main_content, alt_rows_css_def=alt_rows_css_def
    )
    html_unknown = HTML_DOC_TEMPLATE.format(
        num_cols=num_cols, content=unknown_content, alt_rows_css_def=alt_rows_css_def
    )
    return html_main, html_unknown


def tag_creator_dict(priv_dict):
    """Given a single private dict source, list tags that appear in multiple private creators"""
    # Invert the dict from creator: (tag: (VR, VM, name, is_retired))
    #   to tag: {creator: [(VR, VM, name, is_retired)]
    inverted = defaultdict(lambda: defaultdict(list))
    for creator, tagdict in priv_dict.items():
        for tag, vals in tagdict.items():
            inverted[tag][creator].append(vals)
    return inverted


if __name__ == "__main__":
    from dicom_private.dicts.dcmtk import dcmtk_dict
    from dicom_private.dicts.dicom3tools import dicom3tools_dict
    from dicom_private.dicts.gdcm import gdcm_dict
    from dicom_private.dicts.tcia import tcia_dict
    from dicom_private.dicts.DICOM_safe import safe_private_dict

    source_dicts = (
        dcmtk_dict,
        dicom3tools_dict,
        gdcm_dict,
        tcia_dict,
        safe_private_dict,
    )
    source_names = ["DCMTK", "dicom3tools", "GDCM", "TCIA", "DICOM safe"]

    union_dict = make_union_dict(source_dicts)
    # for creator in ("SIEMENS CSA HEADER", "SIEMENS CSA NON-IMAGE", "SIEMENS CSA REPORT", "SIEMENS CT APPL DATASET"):
    #     tbl, contrib = make_creator_compare_table(union_dict[creator], source_names)
    #     print(contrib)

    html, unknowns = html_compare(source_dicts, source_names)

    main_file = REPORT_PATH / "index.html"
    unknowns_file = REPORT_PATH / "unknowns.html"
    print(f"Write {main_file}")
    with open(main_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Write {unknowns_file}")
    with open(unknowns_file, "w", encoding="utf-8") as f:
        f.write(unknowns)
