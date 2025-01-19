from __future__ import annotations

import importlib.metadata

import dicom_private as m


def test_version():
    assert importlib.metadata.version("dicom_private") == m.__version__
