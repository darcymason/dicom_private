# compare_priv.py
"""Gather various private dicts and output files for easy diff
"""
from collections import defaultdict
import difflib
from dicom_private.core import REPORT_PATH
from html import escape

VR, VM, NAME = range(3)  # index into dict results

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



red = lambda text: f'<span class="diff_sub">{text}</span>'
green = lambda text: f'<span class="diff_add">{text}</span>'
yellow = lambda text: f'<span class="diff_chg">{text}</span>'

def diff_new(old, new):
    codes = difflib.SequenceMatcher(a=old, b=new).get_opcodes()
    new2 = ""
    had_del = False
    if new in ("Unknown", "?"):
        return new
    for code in codes:
        op = code[0]
        if op == "equal": 
            new2 += new[code[3]:code[4]]
        elif op == "delete":
            new2 += red(old[code[1]:code[2]])
            had_del = True
        elif op == "insert":
            new2 += green(new[code[3]:code[4]])
        elif op == "replace":
            new2 += yellow(new[code[3]:code[4]])
    return new2 + (f"--> ({new})" if had_del else "")


def html_compare(source_dicts, descriptions):
    """Return a string representing HTML to compare the source dicts"""
    union = compare(source_dicts)
    header = "<div>Tag</div>" + "".join(f"<div>{descr}</div>" for descr in descriptions)
    content = []
    for creator, tag_dict in union.items():
        content.append(f"<h1>{escape(creator)}</h1>")
        content.append('<div class="container">')
        content.append(header)
        for tag, vals in tag_dict.items():
            str_vals = [escape(val[NAME]) if val else "" for val in vals]
            non_empty = [s for s in str_vals if s and s not in ("?", "Unknown")]   
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
        content.append("</div>") # end of container
    content = "\n".join(content)
    num_cols = len(source_dicts) + 1  
    # Can't get nth-child range to work so just list each one  
    alt_rows_css_def = ",\n".join(
        f".container > div:nth-child({2*num_cols}n+{i})"
        for i in range(1, num_cols+1)
    )
    return HTML_DOC_TEMPLATE.format(
        num_cols=num_cols, content=content, alt_rows_css_def=alt_rows_css_def
    )

if __name__ == "__main__":
    from dicom_private.dicts.dcmtk import dcmtk_dict
    from dicom_private.dicts.dicom3tools import dicom3tools_dict
    from dicom_private.dicts.gdcm import gdcm_dict
    from dicom_private.dicts.tcia import tcia_dict

    source_dicts = (dcmtk_dict, dicom3tools_dict, gdcm_dict, tcia_dict)
    descriptions = ["DCMTK", "dicom3tools", "GDCM", "TCIA"]

    # union_dict = compare(source_dicts)
    html = html_compare(source_dicts, descriptions) 
    with open(REPORT_PATH / "index.html", "w", encoding="utf-8") as f:
        f.write(html)