# module2/GeochemDataset.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

process_dict = {
    "XRF26": "Fluxed Glass Disk X-Ray Fluorescence Spectrometry",
    "ICP06": "Inductively Coupled Plasma Atomic Emission Spectroscopy",
    "MS81": "Fluxed-Glass Disk ICP-MS",
    "4ACD81": "Four Acid Digestions before ICP-MS",
    "MS42": "Aqua Regia Digestion before ICP-MS",
    "XRF05": "Powdered X-Ray Fluorescence Spectrometry",
}


def findall(needle, haystack):
    """
    Finds all occurences of a chracter (`needle`) in a string (`haystack`)
    """
    all_occurences = []
    for n, i in enumerate(haystack):
        if i == needle:
            all_occurences.append(n)
    return all_occurences


class ElementalMeasurement:
    """
    Stores data about a measurement process, unit and elemental component.

    Parameters
    ----------
    element_string: str
        Column name of geochemical data spreadsheet, in the format:
        element_unit_XX_process

    Attributes
    ----------
    name: str
        Name of the elemental species analyzed.
    unit: str
        Unit of the measurement.
    process: str
        A description of the process by which the species was measured.
    """
    def __init__(self, element_string):
        element_string_parts = element_string.split("_")
        self.name = element_string_parts[0]
        if element_string_parts[1] == "%":
            self.unit = "percent"
        else:
            self.unit = element_string_parts[1]
        for key, val in process_dict.items():
            if key in element_string_parts[-1]:
                self.process = val

        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val


class GeochemSample:
    """
    Stores data for one geochemical sample.

    Parameters
    ----------
    measurement_objects: list[ElementalMeasurements]
        List of ElementalMeasurement objects.
    measurement_indices: np.ndarray
        Array of indices corresponding elemental measurements in dataset array.
    all_values: pd.Series
        Dataset array with all data available.

    Attributes
    ----------
    <dynamic>
        Based on the number of measurements made on this sample. Attributes
        will correspond to elemental species name (e.g. SiO2).
    """
    def __init__(
        self,
        measurement_objects: list[ElementalMeasurement],
        measurement_indices: np.ndarray,
        all_values: pd.Series
    ):
        measurement_values = all_values.iloc[measurement_indices]
        for meas, val in zip(measurement_objects, measurement_values):
            if not np.isnan(val):
                meas.value = val
                setattr(self, meas.name, meas)

        self._set_metadata(all_values)

    def _set_metadata(self, all_values: pd.Series):
        self.name = all_values.iloc[0]
        self.geologic_series = all_values.iloc[2]
        self.location = (all_values.iloc[3], all_values.iloc[4])
        self.rock_class = all_values.iloc[6]
        self.rock_type = all_values.iloc[7]
        self.rock_name = all_values.iloc[8]
        self.desc = all_values.iloc[9]
        self.weight = all_values.iloc[10]

    def pull_data(self, element_type: str = "major"):
        if element_type == "major":
            unit_case = "percent"
        elif element_type == "minor":
            unit_case = "ppm"
        elements = {}
        for elem in self.__dict__.keys():
            meas = getattr(self, elem)
            if isinstance(meas, ElementalMeasurement):
                if meas.unit == unit_case:
                    elements[meas.name] = meas.value

        return elements

    def spider_plot(
        self,
        ax,
        element_type: str = 'major',
        show_line: bool = True,
        **plot_kwargs
    ):
        """
        Make a spider plot of the sample element data.
        """
        valid_element_types = ["major", "minor"]
        if element_type not in valid_element_types:
            raise ValueError(f"{element_type} is an invalid element type.")

        if show_line:
            ls = "-"
        else:
            ls = ""

        element_subset_dict = self.pull_data(element_type)
        num_subset = len(element_subset_dict)

        elem_vals = np.array(list(element_subset_dict.values()))
        good_idx = elem_vals > 1
        elem_vals = elem_vals[good_idx]
        ax.plot(
            np.arange(num_subset)[good_idx],
            elem_vals,
            linestyle=ls, marker='o', **plot_kwargs
        )
        ax.set_xticks(np.arange(num_subset), element_subset_dict.keys())

        ax.tick_params(axis='x', labelrotation=45)
        title_string = f"Sample: {self.name} ({self.rock_type} " \
                       f"{self.rock_name})"
        ax.set_title(title_string)


class GeochemStandard:
    """
    Specialized GeochemSample-like class for standards.

    Parameters
    ----------
    measurement_objects: list[ElementalMeasurements]
        List of ElementalMeasurement objects.
    measurement_indices: np.ndarray
        Array of indices corresponding elemental measurements in dataset array.
    all_values: pd.Series
        Dataset array with all data available.
    """
    def __init__(
        self,
        measurement_objects: list[ElementalMeasurement],
        measurement_indices: np.ndarray,
        all_values: pd.Series
    ):
        measurement_values = all_values.iloc[measurement_indices]
        for meas, val in zip(measurement_objects, measurement_values):
            if not np.isnan(val):
                meas.value = val
                setattr(self, meas.name, meas)

        self.name = all_values.iloc[0]


class GeochemDataset:
    """
    Easy access to a geochemical dataset in an excel file.

    Parameters
    ----------
    dataset: Path-like or pd.DataFrame
        Either a path to an excel file or a DataFrame corresponding to the
        geochemical data you would like to visualize or analyze.

    Attributes
    ----------
    samples: list[GeochemSample]
        List of geochemical samples in the dataset.
    """
    def __init__(self, dataset):
        if (type(dataset) is str) | isinstance(dataset, Path):
            dataset = pd.read_csv(dataset, index_col=0)
        elif type(dataset) is pd.DataFrame:
            pass
        else:
            raise ValueError(f"Invalid dataset type: {type(dataset)}.")

        self.samples = []
        self.standards = []

        for row in range(dataset.shape[0]):
            em_list, meas_idx = parse_elemental_measurements(
                list(dataset.columns)
            )
            if dataset.iloc[row, 6] == "Standard":
                standard = GeochemStandard(
                    em_list,
                    meas_idx,
                    dataset.iloc[row]
                )
                self.standards.append(standard)
            else:
                samp = GeochemSample(
                    em_list,
                    meas_idx,
                    dataset.iloc[row]
                )
                self.samples.append(samp)


def parse_elemental_measurements(
    column_names: list[str]
) -> list[ElementalMeasurement]:
    """
    Parses through columns names of the dataset to find elemental measurements.

    Parameters
    ----------
    column_names: list[str]
        List of colummn name strings.

    Returns
    -------
    elemental_measurements: list[ElementalMeasurements]
        List of elemental measurement objects.
    measurement_indices: np.ndarray
        Array of indices that correspond to measurement values.
    """
    elemental_measurements = []
    measurement_indices = []
    for idx, i in enumerate(column_names):
        if len(findall("_", i)) > 1 and \
           ("LOI" not in i) and \
           ("Total" not in i) and \
           ("Rcvd" not in i):
            elemental_measurements.append(ElementalMeasurement(i))
            measurement_indices.append(idx)
    return elemental_measurements, np.array(measurement_indices)


if __name__ == "__main__":
    from matplotlib.lines import Line2D
    # Getting path stuff sorted out. Put your local path here!
    from pathlib import Path
    fp = Path("C:/Users/zvig/Desktop/python_code/umdgeopy/module2/"
              "sample_geochemical_data.csv")

    # Creating a GeoChemDataset object
    gd = GeochemDataset(fp)

    # Plotting the major element spider plots for all granite samples.
    def compare_granite_ultramafic(
        ax,
        element_type: str = "major",
        logscale: bool = False
    ):
        for n, sample in enumerate(gd.samples):
            if "granite" in sample.rock_name:
                sample.spider_plot(
                    ax, element_type=element_type, color="black", alpha=0.6
                )
            elif "ultramafic" in sample.rock_name:
                sample.spider_plot(
                    ax, element_type=element_type, color="red", alpha=0.6
                )
            elif "intermediate" in sample.rock_name:
                sample.spider_plot(
                    ax, element_type=element_type, color="orange", alpha=0.6
                )
        legend_elems = [
            Line2D([0], [0], color="black", label="Granites"),
            Line2D([0], [0], color="red", label="Ultramafics"),
            Line2D([0], [0], color="orange", label="Ungrp. Intermediate Rocks")
        ]
        ax.legend(handles=legend_elems)
        title_str = element_type.capitalize() + \
            " Elements: Granite vs. Ultramafics"
        ax.set_title(title_str)

        if logscale:
            ax.set_yscale('log')

    f, [ax1, ax2] = plt.subplots(2, 1, figsize=(17, 10), tight_layout=True)
    compare_granite_ultramafic(ax1, "major")
    compare_granite_ultramafic(ax2, "minor", logscale=True)
    plt.show()
