from pathlib import Path

import pandas as pd
import yaml


class MultiTrack:
    """
    A multitrack recording from medleyDB.
    """

    def __init__(self, track_name: str) -> None:
        self.track_name = track_name
        self._mdb_resource_dir = Path(__file__).parent / "resources"

        self.has_bleed = None
        """Whether the track has bleed, aka audio leeking from other instruments in stems"""
        self.instruments = None
        """An ordered list of instruments for each stem"""
        self.mix_filename = None
        """The name of the mixed audio in MedleyDB"""
        self._activations = None
        """Activation confidence"""
        self._load_metadata()

    @property
    def activations(self) -> pd.DataFrame:
        """
        Get activation confidences for each stem.
        """
        if self._activations is None:
            activation_path = self._mdb_resource_dir / "annotations" / (self.track_name + "_ACTIVATION_CONF.lab")
            self._activations = pd.read_csv(activation_path, delimiter=",").set_axis(
                ["time"] + self.instruments, axis=1
            )
        return self._activations

    def _load_metadata(self) -> None:
        """
        Read the medatada file.
        """
        metadata_path = self._mdb_resource_dir / "metadata" / (self.track_name + "_METADATA.yaml")
        if not metadata_path.exists():
            raise ValueError("This track is not part of MedleyDB")
        with (metadata_path).open("r") as file:
            metadata = yaml.safe_load(file)
        self.has_bleed = metadata["has_bleed"] == "yes"
        self.mix_filename = metadata["mix_filename"]
        instruments = []

        for stem_data in metadata["stems"].values():
            instruments.append(stem_data["instrument"].lower())
        self.instruments = instruments
