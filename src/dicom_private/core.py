# Copyright (c) 2025 Darcy Mason and contributors. All rights reserved.
# See LICENSE file for details
"""Shared routines and constants for private dict generators
"""
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT_PATH = HERE / "dicts"
OUT_PATH.mkdir(exist_ok=True)


# From pydicom's generate_private_dict script,
# modified to add the Type info directly
def write_dict(dict_entries, filename, *, docstring, py_name):
    """Write the `py_name` dict to file `filename`.

    Dict Format
    -----------
    private_dictionaries = {
        'CREATOR_1' : {
            '0029xx00': ('US', '1', 'Unknown', ''),
            '0029xx01': ('US', '1', 'Unknown', ''),
        },
        ...
        'CREATOR_N' : {
            '0029xx00': ('US', '1', 'Unknown', ''),
            '0029xx01': ('US', '1', 'Unknown', ''),
        },
    }

    Parameters
    ----------
    dict_entries: dict
        The completed private creator/tag dictionary to write as Python code
    filename : str
        The file name to write the dict to.
    docstring : str
        A Python docstring to include in the output .py file
    py_name : str
        The variable name for the dictionary written in the .py file
    """
    filepath = OUT_PATH / filename
    print(f"Writing python file {filepath}...", end="")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f'"""\n{docstring}"""\n')
        f.write(
            f"\n{py_name}: dict[str, dict[str, tuple[str, str, str, str]]] = {{\n"
        )
        for creator, tagdict in sorted(dict_entries.items()):
            f.write(f"    '{creator}': {{\n")
            for tag, (vr, vm, name) in tagdict.items():
                quote = '"' if "'" in name else "'"
                f.write(
                    f"""        '{tag}': ('{vr}', '{vm}', {quote}{name}{quote}, ''),\n"""
                )
            f.write("    },\n")
        f.write("}\n")
    print(f"Done.")
