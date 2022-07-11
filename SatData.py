# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 7/10/2022
# Description:

import json


class SatData:
    """___"""

    def __init__(self):
        """___"""
        with open("sat.json", "r") as infile:
            sat_data_dict = json.load(infile)

        self._sat_data = sat_data_dict

    def sav_as_csv(self, dbn_list):
        """___"""

        dbn_list.sort()

        with open("output.csv", "w") as outfile:
            outfile.write("DBN,School Name,Number of Test Takers,Critical Reading Mean,Mathematics Mean,"
                          "Writing Mean" + "\n")

            for value in dbn_list:
                for school in self._sat_data["data"]:
                    if value == self._sat_data["data"][8]:
                        dbn = self._sat_data["data"][8]
                        school_name = self._sat_data["data"][9]
                        test_takers = self._sat_data["data"][10]
                        reading_mean = self._sat_data["data"][11]
                        math_mean = self._sat_data["data"][12]
                        writing_mean = self._sat_data["data"][13]
                        outfile.write(dbn + "," + school_name + "," + test_takers + "," + reading_mean +
                                      "," + math_mean + "," + writing_mean + "\n")


sd = SatData()
dbns = ["02M303", "02M294", "01M450", "02M418"]
sd.save_as_csv(dbns)