# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 7/10/2022
# Description: Creates a dictionary of SAT data and returns a .csv file containing a list of data based upon DBN input,
#                sorted by DBN.

import json


class SatData:
    """Creates a dictionary of SAT data and returns a .csv file containing a list of data based upon DBN input,
    sorted by DBN."""

    def __init__(self):
        """Creates a dictionary of SAT data from a passed file."""
        with open("sat.json", "r") as infile:
            sat_data_dict = json.load(infile)

        self._sat_data = sat_data_dict

    def save_as_csv(self, dbn_list):
        """Returns a .csv file containing a list of data based upon DBN input, sorted by DBN."""

        dbn_list.sort()

        with open("output.csv", "w") as outfile:
            outfile.write("DBN,School Name,Number of Test Takers,Critical Reading Mean,Mathematics Mean,"
                          "Writing Mean" + "\n")

            for value in dbn_list:
                for school in self._sat_data["data"]:
                    if value == school[8]:

                        dbn = school[8]
                        school_name = school[9]
                        if "," in school_name:
                            school_name = '"' + school_name + '"'
                        test_takers = school[10]
                        reading_mean = school[11]
                        math_mean = school[12]
                        writing_mean = school[13]

                        outfile.write(dbn + "," + school_name + "," + test_takers + "," + reading_mean +
                                      "," + math_mean + "," + writing_mean + "\n")
