# medleydb_instruments
[![Linter Actions Status](https://github.com/Seon82/medleydb_instruments/actions/workflows/lint.yml//badge.svg?branch=main)](https://github.com/Seon82/medleydb_instruments/actions)

`medleydb_instruments` is a tool to seemlessly query MedleyDB annotations and instrument metadata.

The [MedleyDB 1.0 and 2.0](https://medleydb.weebly.com/) datasets don't provide annotations or metadata, only raw audio files. The authors provide [an official github repo](https://github.com/marl/medleydb) containing metadata, but it is painful to install and can be quite complex to use. 

## Installation
Simply run: `pip install medleydb_instruments`

## Quickstart
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

