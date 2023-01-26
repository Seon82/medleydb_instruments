# 🎷 medleydb-instruments
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/medleydb-instruments)](https://pypi.org/project/medleydb-instruments/)
 [![PyPI version](https://badge.fury.io/py/medleydb-instruments.svg)](https://badge.fury.io/py/medleydb-instruments)
 [![Linter Actions Status](https://github.com/Seon82/medleydb_instruments/actions/workflows/lint.yml//badge.svg?branch=master)](https://github.com/Seon82/medleydb_instruments/actions)

`medleydb-instruments` is a tool used to seemlessly query MedleyDB annotations and instrument metadata.

The [MedleyDB 1.0 and 2.0](https://medleydb.weebly.com/) datasets don't provide annotations or metadata, only raw audio files. The authors provide [an official github repo](https://github.com/marl/medleydb) containing metadata, but it is painful to install and can be quite complex to use. 

## Installing
Install with `pip` or your favorite PyPI package manager.

```python -m pip install medleydb-instruments```

## Example
```python
import medleydb_instruments as mdb

track = mdb.MultiTrack("AcDc_BackInBlack")
# Get a list of instruments present in the track
instrument_list = track.instruments
# Determine if the recording has bleed
has_bleed = track.has_bleed
# Get a dataframe of instrument activations
activations_df = track.activations
```

