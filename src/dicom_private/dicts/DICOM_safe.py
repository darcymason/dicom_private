"""
DICOM private dictionary auto-generated by make_dcm_safe_private.py.

Data generated 2025-02-01 10:48 from
https://dicom.nema.org/medical/dicom/current/source/docbook/part15/part15.xml

The outer dictionary key is the Private Creator name ("owner"), while the inner
dictionary key is a map of DICOM tag to (VR, VM, name, is_retired).
"""

safe_private_dict: dict[str, dict[str, tuple[str, str, str, str]]] = {
    'ELSCINT1': {
        '00E1xx21': ('DS', '1', 'DLP', ''),
        '00E1xx50': ('DS', '1', 'Acquisition Duration', ''),
        '01E1xx26': ('CS', '1', 'Phantom Type', ''),
        '01F1xx01': ('CS', '1', 'Acquisition Type', ''),
        '01F1xx07': ('DS', '1', 'Table Velocity', ''),
        '01F1xx26': ('DS', '1', 'Pitch', ''),
        '01F1xx27': ('DS', '1', 'Rotation Time', ''),
    },
    'GEIIS PACS': {
        '0903xx10': ('US', '1', 'Reject Image Flag', ''),
        '0903xx11': ('US', '1', 'Significant Flag', ''),
        '0903xx12': ('US', '1', 'Confidential Flag', ''),
    },
    'GEMS_ACQU_01': {
        '0019xx23': ('DS', '1', 'Table Speed [mm/rotation]', ''),
        '0019xx24': ('DS', '1', 'Mid Scan Time [sec]', ''),
        '0019xx27': ('DS', '1', 'Rotation Speed (Gantry Period)', ''),
        '0019xx9E': ('LO', '1', 'Internal Pulse Sequence Name', ''),
    },
    'GEMS_HELIOS_01': {
        '0045xx01': ('SS', '1', 'Number of Macro Rows in Detector', ''),
        '0045xx02': ('FL', '1', 'Macro width at ISO Center', ''),
    },
    'GEMS_PARM_01': {
        '0043xx27': ('SH', '1', 'Scan Pitch Ratio in the form "n.nnn:1"', ''),
        '0043xx39': ('IS', '4', '1stvalue is B Value', ''),
        '0043xx6F': ('DS', '3-4', 'Scanner Table Entry + Gradient Coil Selected', ''),
    },
    'GEMS_SERS_01': {
        '0025xx07': ('SL', '1', 'Images in Series', ''),
    },
    'HOLOGIC, Inc.': {
        '7E01xx01': ('LO', '1', 'Codec Version', ''),
        '7E01xx02': ('SH', '1', 'Codec Content Type', ''),
        '7E01xx10': ('SQ', '1', 'High Resolution Data Sequence', ''),
        '7E01xx11': ('SQ', '1', 'Low Resolution Data Sequence', ''),
        '7E01xx12': ('OB', '1', 'Codec Content', ''),
    },
    'NQHeader': {
        '0099xx01': ('UI', '1', 'Version', ''),
        '0099xx02': ('UI', '1', 'Analyzed Series UID', ''),
        '0099xx04': ('SS', '1', 'Return Code', ''),
        '0099xx05': ('LT', '1', 'Return Message', ''),
        '0099xx10': ('FL', '1', 'MI', ''),
        '0099xx20': ('SH', '1', 'Units', ''),
        '0099xx21': ('FL', '1', 'ICV', ''),
    },
    'NQLeft': {
        '0199xx01': ('FL', '1', 'Left Cortical White Matter', ''),
        '0199xx02': ('FL', '1', 'Left Cortical Gray Matter', ''),
        '0199xx03': ('FL', '1', 'Left 3rd Ventricle', ''),
        '0199xx04': ('FL', '1', 'Left 4th Ventricle', ''),
        '0199xx05': ('FL', '1', 'Left 5th Ventricle', ''),
        '0199xx06': ('FL', '1', 'Left Lateral Ventricle', ''),
        '0199xx07': ('FL', '1', 'Left Inferior Lateral Ventricle', ''),
        '0199xx08': ('FL', '1', 'Left Inferior CSF', ''),
        '0199xx09': ('FL', '1', 'Left Cerebellar White Matter', ''),
        '0199xx0A': ('FL', '1', 'Left Cerebellar Gray Matter', ''),
        '0199xx0B': ('FL', '1', 'Left Hippocampus', ''),
        '0199xx0C': ('FL', '1', 'Left Amygdala', ''),
        '0199xx0D': ('FL', '1', 'Left Thalamus', ''),
        '0199xx0E': ('FL', '1', 'Left Caudate', ''),
        '0199xx0F': ('FL', '1', 'Left Putamen', ''),
        '0199xx10': ('FL', '1', 'Left Pallidum', ''),
        '0199xx11': ('FL', '1', 'Left Ventral Diencephalon', ''),
        '0199xx12': ('FL', '1', 'Left Nucleus Accumbens', ''),
        '0199xx13': ('FL', '1', 'Left Brain Stem', ''),
        '0199xx14': ('FL', '1', 'Left Exterior CSF', ''),
        '0199xx15': ('FL', '1', 'Left WM Hypo', ''),
        '0199xx16': ('FL', '1', 'Left Other', ''),
    },
    'NQRight': {
        '0299xx01': ('FL', '1', 'Right Cortical White Matter', ''),
        '0299xx02': ('FL', '1', 'Right Cortical Gray Matter', ''),
        '0299xx03': ('FL', '1', 'Right 3rd Ventricle', ''),
        '0299xx04': ('FL', '1', 'Right 4th Ventricle', ''),
        '0299xx05': ('FL', '1', 'Right 5th Ventricle', ''),
        '0299xx06': ('FL', '1', 'Right Lateral Ventricle', ''),
        '0299xx07': ('FL', '1', 'Right Inferior Lateral Ventricle', ''),
        '0299xx08': ('FL', '1', 'Right Inferior CSF', ''),
        '0299xx09': ('FL', '1', 'Right Cerebellar White Matter', ''),
        '0299xx0A': ('FL', '1', 'Right Cerebellar Gray Matter', ''),
        '0299xx0B': ('FL', '1', 'Right Hippocampus', ''),
        '0299xx0C': ('FL', '1', 'Right Amygdala', ''),
        '0299xx0D': ('FL', '1', 'Right Thalamus', ''),
        '0299xx0E': ('FL', '1', 'Right Caudate', ''),
        '0299xx0F': ('FL', '1', 'Right Putamen', ''),
        '0299xx10': ('FL', '1', 'Right Pallidum', ''),
        '0299xx11': ('FL', '1', 'Right Ventral Diencephalon', ''),
        '0299xx12': ('FL', '1', 'Right Nucleus Accumbens', ''),
        '0299xx13': ('FL', '1', 'Right Brain Stem', ''),
        '0299xx14': ('FL', '1', 'Right Exterior CSF', ''),
        '0299xx15': ('FL', '1', 'Right WM Hypo', ''),
        '0299xx16': ('FL', '1', 'Right Other', ''),
    },
    'Philips Imaging DD 001': {
        '2001xx01': ('FL', '1', 'MR Image Chemical Shift', ''),
        '2001xx02': ('IS', '1', 'MR Image Chemical Shift Number', ''),
        '2001xx03': ('FL', '1', 'MR Image Diffusion B-Factor', ''),
        '2001xx04': ('CS', '1', 'MR Image Diffusion Direction', ''),
        '2001xx05': ('SS', '1', 'Graphic Annotation Parent ID', ''),
        '2001xx06': ('CS', '1', 'MR Image Enhanced', ''),
        '2001xx07': ('CS', '1', 'MR Image Type Edes', ''),
        '2001xx08': ('IS', '1', 'MR Image Phase Number', ''),
        '2001xx09': ('FL', '1', 'MR Image Prepulse Delay', ''),
        '2001xx0A': ('IS', '1', 'Image Plane Number', ''),
        '2001xx0B': ('CS', '1', 'Image Plane Orientation', ''),
        '2001xx0C': ('CS', '1', 'MR Series Arrhythmia Rejection', ''),
        '2001xx0E': ('CS', '1', 'MR Series Cardiac Cycled', ''),
        '2001xx0F': ('SS', '1', 'MR Series Cardiac Gate Width', ''),
        '2001xx10': ('CS', '1', 'MR Series Cardiac Sync', ''),
        '2001xx11': ('FL', '1', 'MR Series Diffusion Echo Time', ''),
        '2001xx12': ('CS', '1', 'MR Series Dynamic Series', ''),
        '2001xx13': ('SL', '1', 'MR Series Epi Factor', ''),
        '2001xx14': ('SL', '1', 'MR Series Nr Of Echoes', ''),
        '2001xx15': ('SS', '1', 'MR Series Nr Of Locations', ''),
        '2001xx16': ('SS', '1', 'MR Series Nr Of Phase Contrast Directions', ''),
        '2001xx17': ('SL', '1', 'MR Series Nr Of Phases', ''),
        '2001xx18': ('SL', '1', 'MR Series Nr Of Slices', ''),
        '2001xx19': ('CS', '1', 'MR Series Partial Matrix Scanned', ''),
        '2001xx1A': ('FL', '3', 'MR Series Pc Velocity', ''),
        '2001xx1B': ('FL', '1', 'MR Series Prepulse Delay', ''),
        '2001xx1C': ('CS', '1', 'MR Series Prepulse Type', ''),
        '2001xx1D': ('IS', '1', 'MR Series Reconstruction Number', ''),
        '2001xx1E': ('CS', '1', 'MR Series Reformat Accuracy', ''),
        '2001xx1F': ('CS', '1', 'MR Series Respiration Sync', ''),
        '2001xx21': ('CS', '1', 'MR Series Sel Part Inversion Recovery', ''),
        '2001xx22': ('FL', '1', 'MR Series Water Fat Shift', ''),
        '2001xx23': ('DS', '1', 'MR Series Flip Angle', ''),
        '2001xx24': ('CS', '1', 'MR Series Is Interactive', ''),
        '2001xx25': ('SH', '1', 'MR Series Echo Time Display', ''),
        '2001xx26': ('CS', '1', 'Presentation State Subtraction Active', ''),
        '2001xx27': ('CS', '1', 'Edge Enhancement Kernel Size', ''),
        '2001xx28': ('FL', '1', 'Edge Enhancement Gain Factor Sub', ''),
        '2001xx29': ('FL', '1', 'Edge Enhancement Gain Factor', ''),
        '2001xx2A': ('CS', '1', 'Edge Enhancement Taste Adapt Sub', ''),
        '2001xx2B': ('CS', '1', 'Edge Enhancement Taste Adapt', ''),
        '2001xx2C': ('FL', '1', 'Harmonization Factor', ''),
        '2001xx2D': ('SS', '1', 'Stack Number Of Slices', ''),
        '2001xx2E': ('CS', '1', 'Harmonization Kernel Size', ''),
        '2001xx2F': ('FL', '1', 'Harmonization Gain', ''),
        '2001xx30': ('UL', '1', 'Log Subtraction Gain Step Taste', ''),
        '2001xx31': ('US', '1', 'Mixing Nr Of Mask Image Numbers', ''),
        '2001xx32': ('FL', '1', 'Stack Radial Angle', ''),
        '2001xx33': ('CS', '1', 'Stack Radial Axis', ''),
        '2001xx34': ('CS', '1', 'Mixing Mask Operation Type', ''),
        '2001xx35': ('SS', '1', 'Stack Slice Number', ''),
        '2001xx36': ('CS', '1', 'Stack Type', ''),
        '2001xx37': ('CS', '1', 'Mixing Operation Type', ''),
        '2001xx38': ('FL', '1', 'Overlay Mix Factor', ''),
        '2001xx39': ('FL', '1', 'Overscan Factor', ''),
        '2001xx3A': ('CS', '1', 'Pixel Shift', ''),
        '2001xx3B': ('FL', '4', 'Pixel Shift Split Line Coordinates', ''),
        '2001xx3C': ('FL', '2', 'Pixel Shift Shift Vectora', ''),
        '2001xx3D': ('UL', '1', 'Contour Fill Color', ''),
        '2001xx3E': ('FL', '2', 'Pixel Shift Shift Vectorb', ''),
        '2001xx3F': ('CS', '1', 'Displayed Area Zoom Interpolation Meth', ''),
        '2001xx40': ('CS', '1', 'Pixel Shift Split Screen', ''),
        '2001xx41': ('FL', '1', 'Subtraction Land Marking Factor', ''),
        '2001xx42': ('CS', '1', 'Subtraction Land Marking Active', ''),
        '2001xx43': ('IS', '2', 'Ellips Displ Shut Major Ax Frst End Pnt', ''),
        '2001xx44': ('IS', '2', 'Ellips Displ Shut Major Ax Scnd End Pnt', ''),
        '2001xx45': ('IS', '2', 'Ellips Displ Shut Other Ax Frst End Pnt', ''),
        '2001xx46': ('CS', '1', 'Graphic Line Style', ''),
        '2001xx47': ('FL', '1', 'Graphic Line Width', ''),
        '2001xx48': ('SS', '1', 'Graphic Annotation Id', ''),
        '2001xx49': ('IS', '1', 'Trace First Image', ''),
        '2001xx4A': ('CS', '1', 'Trace Taste', ''),
        '2001xx4B': ('CS', '1', 'Interpolation Method', ''),
        '2001xx4C': ('CS', '1', 'Poly Line Begin Point Style', ''),
        '2001xx4D': ('CS', '1', 'Poly Line End Point Style', ''),
        '2001xx4E': ('CS', '1', 'Window Smoothing Taste', ''),
        '2001xx4F': ('FD', '1', 'Harmonization Offset', ''),
        '2001xx50': ('LO', '1', 'Graphic Marker Type', ''),
        '2001xx51': ('IS', '1', 'Overlay Plane Id', ''),
        '2001xx53': ('CS', '1', 'Presentation Gl Trafo Invert', ''),
        '2001xx54': ('FL', '1', 'Contour Fill Transparency', ''),
        '2001xx55': ('UL', '1', 'Graphic Line Color', ''),
        '2001xx56': ('CS', '1', 'Graphic Type', ''),
        '2001xx57': ('CS', '1', 'Log Subtraction Taste', ''),
        '2001xx58': ('UL', '1', 'Series Xray Contrast Transfer Taste', ''),
        '2001xx59': ('IS', '1', 'Curve Id', ''),
        '2001xx5A': ('ST', '1', 'Graphic Annotation Model', ''),
        '2001xx5D': ('ST', '1', 'Measurement Text Units', ''),
        '2001xx5E': ('ST', '1', 'Measurement Text Type', ''),
        '2001xx5F': ('SQ', '1-n', 'Stack Sequence', ''),
        '2001xx60': ('SL', '1', 'MR Series Nr Of Stacks', ''),
        '2001xx61': ('CS', '1', 'Series Transmitted', ''),
        '2001xx62': ('CS', '1', 'Series Committed', ''),
        '2001xx63': ('CS', '1', 'Examination Source', ''),
        '2001xx64': ('SH', '1', 'Text Type', ''),
        '2001xx65': ('SQ', '1-n', 'Overlay Plane Sequence', ''),
        '2001xx66': ('SQ', '1-n', 'Image Curve', ''),
        '2001xx67': ('CS', '1', 'Linear Presentation Gl Trafo Shape Sub', ''),
        '2001xx68': ('SQ', '1-n', 'Modality Gl Trafo Sequence', ''),
        '2001xx69': ('SQ', '1-n', 'Display Shutter Sequence', ''),
        '2001xx6A': ('SQ', '1-n', 'Spatial Transformation Sequence', ''),
        '2001xx6B': ('SQ', '1-n', 'Edge Enhancement Sequence', ''),
        '2001xx6D': ('LO', '1', 'Text Font', ''),
        '2001xx6E': ('SH', '1', 'Series Type', ''),
        '2001xx6F': ('SQ', '1-n', 'Mixing Sequence', ''),
        '2001xx71': ('CS', '1', 'Graphic Constraint', ''),
        '2001xx72': ('IS', '2', 'Ellips Displ Shut Other Ax Scnd End Pnt', ''),
        '2001xx73': ('SQ', '1-n', 'Referenced Mask Image Sequence', ''),
        '2001xx74': ('DS', '1-n', 'Window Center Sub', ''),
        '2001xx75': ('DS', '1-n', 'Window Width Sub', ''),
        '2001xx76': ('UL', '1', 'Presentation State Xray Contrast Transfer Taste', ''),
        '2001xx77': ('CS', '1', 'Gl Trafo Type', ''),
        '2001xx79': ('SQ', '1-n', 'Harmonisation Sequence', ''),
        '2001xx7A': ('FL', '1', 'Window Rounding Factor', ''),
        '2001xx7B': ('IS', '1', 'MR Series Acquisition Number', ''),
        '2001xx7C': ('UL', '1', 'Frame Number', ''),
        '2001xx7D': ('OW/OB', '1', 'Frame Pixel Data', ''),
        '2001xx7E': ('US', '1', 'Edge Enhancement Gain Taste', ''),
        '2001xx7F': ('US', '1', 'Edge Enhancement Gain Taste Sub', ''),
        '2001xx80': ('LO', '1', 'Text Anchor Point Alignment', ''),
        '2001xx81': ('IS', '1', 'MR Series Nr Of Dynamic Scans', ''),
        '2001xx82': ('IS', '1', 'MR Series Echo Train Length', ''),
        '2001xx83': ('DS', '1', 'MR Series Imaging Frequency', ''),
        '2001xx84': ('DS', '1', 'MR Series Inversion Time', ''),
        '2001xx85': ('DS', '1', 'MR Series Magnetic Field Strength', ''),
        '2001xx86': ('IS', '1', 'MR Series Nr Of Phase Encoding Steps', ''),
        '2001xx87': ('SH', '1', 'MR Series Nucleus', ''),
        '2001xx88': ('DS', '1', 'MR Series Number Of Averages', ''),
        '2001xx89': ('DS', '1', 'MR Series Percent Phase Field Of View', ''),
        '2001xx8A': ('DS', '1', 'MR Series Percent Sampling', ''),
        '2001xx8B': ('SH', '1', 'MR Series Transmitting Coil', ''),
        '2001xx8C': ('CS', '0-n', 'Needs Processing', ''),
        '2001xx90': ('LO', '1', 'Text Foreground Color', ''),
        '2001xx91': ('LO', '1', 'Text Background Color', ''),
        '2001xx92': ('LO', '1', 'Text Shadow Color', ''),
        '2001xx93': ('LO', '1', 'Text Style', ''),
        '2001xx94': ('LO', '1', 'Processing Order Specialization', ''),
        '2001xx9A': ('SQ', '1-n', 'Graphic Number Sequence', ''),
        '2001xx9B': ('UL', '1', 'Graphic Number', ''),
        '2001xx9D': ('LO', '1', 'Subtraction Type', ''),
        '2001xx9F': ('US', '2', 'Pixel Processing Kernel Size', ''),
        '2001xxA1': ('CS', '1', 'Is Raw Image', ''),
        '2001xxA2': ('US', '1', 'Log Subtraction Curve Taste', ''),
        '2001xxA3': ('UL', '1', 'Text Color Foreground', ''),
        '2001xxA4': ('UL', '1', 'Text Color Background', ''),
        '2001xxA5': ('UL', '1', 'Text Color Shadow', ''),
        '2001xxC0': ('UL', '1', 'Content Item Identifier', ''),
        '2001xxC1': ('LO', '1', 'Nested Object Type Name', ''),
        '2001xxC2': ('FD', '1', 'Subtraction Rescale Factor', ''),
        '2001xxC3': ('UL', '1', 'Subtraction Offset', ''),
        '2001xxC5': ('SQ', '0-1', 'Mask Image Lut Sequence', ''),
        '2001xxC6': ('SQ', '0-1', 'Gain Lut Sequence', ''),
        '2001xxC7': ('SQ', '0-1', 'Contrast Image Lut Sequence', ''),
        '2001xxCA': ('SQ', '1', 'Reversed Modality Lut', ''),
        '2001xxCB': ('IS', '1', 'Redundant Overlay Plane Id', ''),
        '2001xxD0': ('AT', '1-n', 'Frame Index Pointer', ''),
        '2001xxD1': ('US', '1-n', 'Index Number Vector', ''),
        '2001xxD2': ('US', '1', 'Frame Detector Number', ''),
        '2001xxD3': ('US', '1', 'Frame Phase Number', ''),
        '2001xxD4': ('US', '1', 'Frame Rotation Number', ''),
        '2001xxD5': ('US', '1', 'Frame Rr Interval Number', ''),
        '2001xxD6': ('US', '1', 'Frame Time Slot Number', ''),
        '2001xxD7': ('US', '1', 'Frame Slice Number', ''),
        '2001xxD8': ('US', '1', 'Frame Angular View Number', ''),
        '2001xxD9': ('US', '1', 'Frame Time Slice Number', ''),
        '2001xxDA': ('CS', '1', 'Is Arrowhead', ''),
        '2001xxDB': ('US', '1', 'PET Rr Interval Index', ''),
        '2001xxDC': ('US', '1', 'PET Time Slot Index', ''),
        '2001xxDD': ('US', '1', 'PET Time Slice Index', ''),
        '2001xxDE': ('US', '1', 'PET Slice Index', ''),
        '2001xxDF': ('UL', '1', 'Voxel Number', ''),
        '2001xxE9': ('SQ', '0-n', 'Per Frame Voxels Functional Group', ''),
        '2001xxF1': ('FL', '6', 'MR Image Prospective Motion Correction', ''),
        '2001xxF2': ('FL', '1-n', 'MR Image Retrospective Motion Correction', ''),
        '2001xxF3': ('CS', '1', 'Dynamic Linear Voigl Trafo', ''),
        '2001xxF4': ('UL', '1', 'Color Key', ''),
        '2001xxF5': ('CS', '1', 'Rotated Text Allowed', ''),
        '2001xxF6': ('UL', '1', 'Number Of Represented Images', ''),
        '2001xxF7': ('LO', '0-n', 'Data Type Icons', ''),
        '2001xxF9': ('SQ', '0-n', 'Flagging Sequence', ''),
        '2001xxFB': ('SQ', '0-1', 'Bookmark Sequence', ''),
        '2001xxFC': ('SQ', '0-1', 'Ris Code Sequence', ''),
        '2001xxFD': ('SQ', '0-n', 'Workflow Step Sequence', ''),
        '2001xxFF': ('OW/OB', '1', 'Volume Pixel', ''),
    },
    'Philips Imaging DD 002': {
        '2001xx01': ('US', '1', 'Edr Setgp', ''),
        '2001xx02': ('FD', '1', 'Edr Setsk', ''),
        '2001xx03': ('CS', '1', 'Um Rank Type', ''),
        '2001xx04': ('SS', '1', 'Um Rank Number', ''),
        '2001xx05': ('FD', '1', 'Um Rank Enhancement', ''),
        '2001xx06': ('US', '1', 'Um Kernel Size', ''),
        '2001xx07': ('CS', '1', 'Um Gamma Type', ''),
        '2001xx08': ('FD', '1', 'Um Gamma Angle', ''),
        '2001xx09': ('FD', '1', 'Um Gamma Shift', ''),
        '2001xx0A': ('FD', '1', 'Um Gamma Center', ''),
        '2001xx0B': ('FD', '1', 'Drr Contrast Equalization', ''),
        '2001xx0C': ('US', '1', 'Drr Contrast Equalization Kernel Size', ''),
        '2001xx0D': ('CS', '1', 'Drr Sharp Lut Type', ''),
        '2001xx0E': ('FD', '1', 'Drr Sharpening', ''),
        '2001xx0F': ('US', '1', 'Drr Sharp Kernel Size', ''),
        '2001xx10': ('SS', '1', 'Drr Window Width', ''),
        '2001xx11': ('SS', '1', 'Drr Window Level', ''),
        '2001xx12': ('CS', '1', 'Drr Lut Type', ''),
        '2001xx13': ('SS', '1', 'Unique Processing Mode', ''),
        '2001xx14': ('FD', '1', 'Unique Contrast Balance', ''),
        '2001xx15': ('FD', '1', 'Unique Center Density', ''),
        '2001xx16': ('FD', '1', 'Unique Bright Density', ''),
        '2001xx17': ('FD', '1', 'Unique Detail Contrast', ''),
        '2001xx18': ('CS', '1', 'Unique Density Curve', ''),
        '2001xx19': ('FD', '1', 'Unique Density Min', ''),
        '2001xx1A': ('FD', '1', 'Unique Density Max', ''),
        '2001xx1B': ('FD', '1', 'Unique Gamma', ''),
        '2001xx1C': ('FD', '1', 'Unique Gamma Min', ''),
        '2001xx1D': ('FD', '1', 'Unique Gamma Max', ''),
        '2001xx1E': ('FD', '1', 'Unique Structure Preference', ''),
        '2001xx1F': ('FD', '1', 'Unique Noise Limit', ''),
        '2001xx20': ('FD', '1', 'Unique Noise Band', ''),
        '2001xx21': ('FD', '1', 'Unique Noise Step', ''),
        '2001xx22': ('FD', '1', 'Unique Noise Compensation', ''),
        '2001xx23': ('FD', '1', 'Unique Structure Boost', ''),
        '2001xx24': ('FD', '1', 'Unique Strong Contrast Limit', ''),
        '2001xx25': ('FD', '1', 'Unique Strong Contrast Factor', ''),
        '2001xx26': ('FD', '1', 'Unique Structure Boost Offset', ''),
        '2001xx27': ('FD', '1', 'Unique Weak Contrast Limit', ''),
        '2001xx28': ('US', '1', 'Unique Smooth Gain', ''),
        '2001xx29': ('US', '1', 'Unique Level', ''),
        '2001xx2A': ('US', '1', 'Unique Gain Up Single', ''),
        '2001xx2B': ('SS', '1', 'Unique Smh Limit One', ''),
        '2001xx2C': ('FD', '1', 'Unique Film Density Min', ''),
        '2001xx2D': ('FD', '1', 'Unique Film Density Max', ''),
        '2001xx2E': ('SS', '1', 'Unique Version', ''),
        '2001xx2F': ('SS', '1', 'Ranger Version', ''),
        '2001xx30': ('SS', '1', 'Ranger Mode', ''),
        '2001xx31': ('SS', '1', 'Ranger Field1', ''),
        '2001xx32': ('SS', '1', 'Ranger Field2', ''),
        '2001xx33': ('SS', '1', 'Ranger Percentile Key1', ''),
        '2001xx34': ('SS', '1', 'Ranger Percentile Key2', ''),
        '2001xx35': ('FD', '1', 'Ranger Dose1', ''),
        '2001xx36': ('FD', '1', 'Ranger Dose2', ''),
        '2001xx37': ('FD', '1', 'Ranger Manual Dose1', ''),
        '2001xx38': ('FD', '1', 'Ranger Manual Dose2', ''),
        '2001xx39': ('CS', '1', 'Unique Rox Shape', ''),
        '2001xx3A': ('SQ', '1', 'Ranger Set Sequence', ''),
        '2001xx3B': ('SQ', '0-n', 'Rox Sequence', ''),
        '2001xx3C': ('SQ', '1-n', 'Xray Edge Enhancement Sequence', ''),
        '2001xx3D': ('SQ', '0-1', 'Edr Lut Sequence', ''),
        '2001xx3E': ('SS', '1', 'Unique Dose Decades', ''),
        '2001xx3F': ('SS', '1', 'Unique Dose Unit', ''),
        '2001xx40': ('SS', '1', 'Unique Density Unit', ''),
        '2001xx50': ('CS', '1', 'Workflow Status', ''),
        '2001xx52': ('LO', '1', 'Workflow Step Id', ''),
        '2001xx53': ('CS', '1', 'Workflow Step Status', ''),
        '2001xx57': ('SQ', '0-1', 'Workflow Step Input Sequence', ''),
        '2001xx58': ('SQ', '0-1', 'Workflow Step Output Sequence', ''),
        '2001xx5A': ('LO', '1', 'Workflow Step Type', ''),
        '2001xx5C': ('LO', '1', 'Workflow Id', ''),
        '2001xx5D': ('UL', '1', 'Pixel Data Representation Rows', ''),
        '2001xx5E': ('UL', '1', 'Pixel Data Representation Columns', ''),
        '2001xx5F': ('SQ', '0-1', 'Private Dicom Extension Sequence', ''),
        '2001xx63': ('ST', '1', 'Isyntax Reference', ''),
        '2001xx64': ('SQ', '0-1', 'Workflow Step Job Params Sequence', ''),
        '2001xx65': ('CS', '1', 'Preserve Aspect', ''),
        '2001xx66': ('CS', '1', 'Interpolated', ''),
        '2001xx67': ('LO', '1', 'Error Flag', ''),
        '2001xx68': ('LO', '1', 'Error Message Id', ''),
        '2001xx6B': ('LO', '0-n', 'Suitable For', ''),
        '2001xx71': ('CS', '1', 'Submit Mpps Job', ''),
        '2001xx72': ('FL', '2', 'Displayed Area Bottom Right Hand Corner Fraction', ''),
        '2001xx73': ('FL', '2', 'Displayed Area Top Left Hand Corner Fraction', ''),
        '2001xx74': ('LO', '1', 'Interpolation Mode', ''),
        '2001xx75': ('SS', '0-n', 'Graphic Annotation Id Reference', ''),
    },
    'Philips Imaging DD 097': {
        '2001xx01': ('SQ', '1', 'View Geometry', ''),
        '2001xx02': ('FD', '3', 'Frame Geometry Origin', ''),
        '2001xx03': ('FD', '2', 'Frame Geometry Extent', ''),
        '2001xx04': ('FD', '6', 'Frame Geometry Orientation', ''),
        '2001xx05': ('SQ', '1-n', 'Visual Sequence', ''),
        '2001xx06': ('SQ', '0-n', 'Cut Sequence', ''),
        '2001xx07': ('FD', '1', 'Visual Opacity', ''),
        '2001xx08': ('SQ', '1', 'Opacity Map Sequence', ''),
        '2001xx0A': ('SQ', '1-n', 'Light Sequence', ''),
        '2001xx0B': ('SQ', '1', 'Color Map Sequence', ''),
        '2001xx0D': ('FD', '1', 'Visual Threshold', ''),
        '2001xx0E': ('SQ', '0-n', 'Scene Sequence', ''),
        '2001xx0F': ('FD', '2', 'Frame Geometry Slab', ''),
        '2001xx12': ('SQ', '1', 'Gradient Map Sequence', ''),
        '2001xx17': ('US', '1', 'Display Rows', ''),
        '2001xx18': ('US', '1', 'Display Columns', ''),
        '2001xx19': ('LO', '1', 'Frame Geometry Type', ''),
        '2001xx1A': ('FD', '1', 'Light Intensity', ''),
        '2001xx1B': ('UL', '1', 'Light Color', ''),
        '2001xx1C': ('FD', '3', 'Light Origin', ''),
        '2001xx1D': ('FD', '3', 'Light Direction', ''),
        '2001xx1E': ('FD', '4-n', 'Color Map Samples', ''),
        '2001xx1F': ('FD', '2-n', 'Opacity Map Samples', ''),
        '2001xx21': ('UL', '1', 'Visual Color', ''),
        '2001xx22': ('FD', '1', 'Illumination Ambient', ''),
        '2001xx23': ('FD', '1', 'Illumination Diffuse', ''),
        '2001xx24': ('FD', '1', 'Illumination Specular', ''),
        '2001xx25': ('FD', '1', 'Illumination Specular Power', ''),
        '2001xx26': ('FD', '1', 'Depth Cue Begin', ''),
        '2001xx27': ('FD', '1', 'Depth Cue Lambda', ''),
        '2001xx28': ('LO', '1', 'Depth Cue Function', ''),
        '2001xx2A': ('LO', '1', 'Cut Set Type', ''),
        '2001xx2B': ('FD', '3', 'Cut Plane Origin', ''),
        '2001xx2C': ('FD', '3', 'Cut Plane Normal', ''),
        '2001xx2D': ('UL', '1', 'Volume Definition Number', ''),
        '2001xx2E': ('SQ', '0-1', 'Volume Mask Sequence', ''),
        '2001xx2F': ('OB', '1', 'Volume Mask Data', ''),
        '2001xx30': ('SL', '3', 'Volume Mask Offset', ''),
        '2001xx31': ('SL', '3', 'Volume Mask Size', ''),
        '2001xx32': ('SL', '2', 'Volume Mask Alignment', ''),
        '2001xx36': ('LO', '1', 'Light Anchor', ''),
        '2001xx37': ('FD', '3', 'Cone Geometry Origin', ''),
        '2001xx38': ('FD', '9', 'Cone Geometry Orientation', ''),
        '2001xx39': ('FD', '1', 'Cone Geometry View Distance', ''),
        '2001xx3A': ('FD', '2', 'Cone Geometry Slab Extent', ''),
        '2001xx3B': ('FD', '2', 'Cone Geometry Field Of View', ''),
        '2001xx3C': ('SQ', '1', 'Intensity Map Sequence', ''),
        '2001xx3D': ('FD', '1-n', 'Intensity Map Samples', ''),
        '2001xx3E': ('SQ', '0-n', 'Mesh Sequence', ''),
        '2001xx40': ('UL', '1', 'Mesh Color', ''),
        '2001xx41': ('LO', '1', 'Mesh Draw Style', ''),
        '2001xx42': ('SQ', '0-n', 'Mesh Section Sequence', ''),
        '2001xx44': ('LO', '1', 'Mesh Section Vertex Connectivity', ''),
        '2001xx45': ('SL', '1', 'Mesh Section Vertex Size', ''),
        '2001xx46': ('LO', '1', 'Mesh Section Vertex Format', ''),
        '2001xx47': ('OB', '1-n', 'Mesh Section Vertex Data', ''),
        '2001xx49': ('SQ', '1', 'Referenced Volume Definition Sequence', ''),
        '2001xx4A': ('OB', '1-n', 'Mesh Section Index Data', ''),
        '2001xx4B': ('SL', '1', 'Mesh Section Index Size', ''),
        '2001xx4C': ('LO', '1', 'Shutter Interaction Type', ''),
        '2001xxA1': ('CS', '1-2', 'Volume Type', ''),
        '2001xxA2': ('FD', '3', 'Volume Origin', ''),
        '2001xxA3': ('FD', '9', 'Volume Axis', ''),
        '2001xxA4': ('FD', '2', 'Volume Pixel Spacing', ''),
        '2001xxA5': ('FD', '1-n', 'Volume Slice Spacing', ''),
        '2001xxA6': ('US', '1', 'Volume Slices', ''),
        '2001xxA8': ('IS', '1-n', 'Referenced Volume Definition Number', ''),
        '2001xxA9': ('SQ', '0-n', 'Linear Modality Gl Trafo Sequence', ''),
        '2001xxAA': ('FD', '1-n', 'Volume Slice Offsets', ''),
        '2001xxAB': ('IS', '1', 'Number Of Volume Definitions', ''),
    },
    'Philips Imaging DD 129': {
        '2001xx00': ('SQ', '1', 'Presentation State Sequence', ''),
        '2001xx01': ('SQ', '1', 'Embedded Original Presentation State Sequence', ''),
        '2001xx02': ('SQ', '0-1', 'Planar Intersection Sequence', ''),
        '2001xx03': ('UL', '1', 'Plane Separator Line Color', ''),
        '2001xx04': ('SQ', '1-n', 'Plane Sequence', ''),
        '2001xx05': ('FD', '4', 'Plane Equation', ''),
        '2001xx06': ('FD', '1', 'Plane Opacity', ''),
        '2001xx07': ('CS', '1', 'Plane Enabled', ''),
        '2001xx08': ('CS', '1', 'Plane Selected', ''),
        '2001xx09': ('UL', '1', 'Plane Highlight Color', ''),
    },
    'Philips MR Imaging DD 001': {
        '2005xx0D': ('FL', '1', 'Scale Intercept', ''),
        '2005xx0E': ('FL', '1', 'Scale Slope', ''),
    },
    'Philips PET Private Group': {
        '7053xx00': ('DS', '1', 'SUV Factor - Multiplying Stored Pixel Values by Rescale Slope then this factor results in SUVbw in g/l', ''),
        '7053xx09': ('DS', '1', 'Activity Concentration Factor - Multiplying Stored Pixel Values by Rescale Slope then this factor results in MBq/ml.', ''),
    },
    'Philips ST80i': {
        '0025xx01': ('OW', '1', 'ST80i Stress Study file data', ''),
    },
    'SIEMENS MR HEADER': {
        '0019xx0C': ('IS', '1', 'B Value', ''),
        '0019xx0D': ('CS', '1', 'Diffusion Directionality', ''),
        '0019xx0E': ('FD', '3', 'Diffusion Gradient Direction', ''),
        '0019xx27': ('FD', '6', 'B Matrix', ''),
    },
    'SIEMENS SYNGO ULTRA-SOUND TOYON DATA STREAMING': {
        '7FD1xx01': ('OB', '1', 'Padding', ''),
        '7FD1xx09': ('UI', '1', 'Version ID', ''),
        '7FD1xx10': ('OB', '1', 'Volume Payload', ''),
        '7FD1xx11': ('OB', '1', 'After Payload', ''),
    },
    'SIEMENS Ultrasound SC2000': {
        '0119xx00': ('LO', '1', 'Acoustic Meta Information Version', ''),
        '0119xx01': ('OB', '1', 'Common Acoustic Meta Information', ''),
        '0119xx02': ('SQ', '1', 'Multi Stream Sequence', ''),
        '0119xx03': ('SQ', '1', 'Acoustic Data Sequence', ''),
        '0119xx04': ('OB', '1', 'Per Transaction Acoustic Control Information', ''),
        '0119xx05': ('UL', '1', 'Acoustic Data Offset', ''),
        '0119xx06': ('UL', '1', 'Acoustic Data Length', ''),
        '0119xx07': ('UL', '1', 'Footer Offset', ''),
        '0119xx08': ('UL', '1', 'Footer Length', ''),
        '0119xx09': ('SS', '1', 'Acoustic Stream Number', ''),
        '0119xx10': ('SH', '1', 'Acoustic Stream Type', ''),
        '0119xx11': ('', '1', 'Stage Timer Time', ''),
        '0119xx12': ('', '1', 'Stop Watch Time', ''),
        '0119xx13': ('IS', '1', 'Volume Rate', ''),
        '0119xx21': ('SH', '1', '', ''),
        '0129xx00': ('SQ', '1', 'MPR View Sequence', ''),
        '0129xx02': ('UI', '1', 'Bookmark UID', ''),
        '0129xx03': ('', '1', 'Plane Origin Vector', ''),
        '0129xx04': ('', '1', 'Row Vector', ''),
        '0129xx05': ('', '1', 'Column Vector', ''),
        '0129xx06': ('SQ', '1', 'Visualization Sequence', ''),
        '0129xx07': ('UI', '1', 'Bookmark UID', ''),
        '0129xx08': ('OB', '1', 'Visualization Information', ''),
        '0129xx09': ('SQ', '1', 'Application State Sequence', ''),
        '0129xx10': ('OB', '1', 'Application State Information', ''),
        '0129xx11': ('SQ', '1', 'Referenced Bookmark Sequence', ''),
        '0129xx12': ('UI', '1', 'Referenced Bookmark UID', ''),
        '0129xx20': ('SQ', '1', 'Cine Parameters Sequence', ''),
        '0129xx21': ('OB', '1', 'Cine Parameters Schema', ''),
        '0129xx22': ('OB', '1', 'Values of Cine Parameters', ''),
        '0129xx29': ('OB', '1', '', ''),
        '0129xx30': ('CS', '1', 'Raw Data Object Type', ''),
        '0139xx01': ('SL', '1', 'Physio Capture ROI', ''),
        '0149xx01': ('FD', '1-n', 'Vector of BROI Points', ''),
        '0149xx02': ('FD', '1-n', 'Start/End Timestamps of Strip Stream', ''),
        '0149xx03': ('FD', '1-n', 'Timestamps of Visible R-waves', ''),
        '7FD1xx01': ('OB', '1', 'Acoustic Image and Footer Data', ''),
        '7FD1xx09': ('UI', '1', 'Volume Version ID', ''),
        '7FD1xx10': ('OB', '1', 'Volume Payload', ''),
        '7FD1xx11': ('OB', '1', 'After Payload', ''),
    },
}
