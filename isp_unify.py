
"""
Project for Week 3 of "Python Data Visualization".
Unify data via common country name.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal




def reconcile_countries_by_name(plot_countries, gdp_countries):
    """
    Inputs:
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country names used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country names from
      gdp_countries The set contains the country codes from
      plot_countries that were not found in gdp_countries.
    """

    # Establish output references.
    output_dict = {}
    output_set = set()

    # Iteration compares the keys of "plot_countries" to the values of
    # "gdp_countries".  If they are identical then they are added to the
    # "output_dict" with key and value both from "plot_countries", if not then
    # they are added to "output_set".
    for key in plot_countries:
        if plot_countries[key] in gdp_countries:
            output_dict[key] = plot_countries[key]
        else:
            output_set.add(key)

    return output_dict, output_set




def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """

    # Establish output references.
    output_dict = {}
    output_set1 = set()
    output_set2 = set()

    # Establish working reference.
    table = {}

    # Open argued "filename" as reference "csvfile".
    with open(gdpinfo['gdpfile'], newline='') as csvfile:
        # With "DictReader" function convert "csvfile" to dictionary as
        # "csvreader".
        csvreader = csv.DictReader(csvfile, delimiter=gdpinfo['separator'], \
        quotechar=gdpinfo['quote'])

        # Iterate over "csvreader" to nest argued "gdpinfo['country_name']" as
        # columns within rows.
        for row in csvreader:
            rowid = row[gdpinfo['country_name']]
            table[rowid] = row

    # Reassign value for each key in "table" to the value of the "table" key
    # "year" from arguments.
    for each in table:
        table[each] = table[each][year]


    for key in plot_countries:
        # If value in "plot_countries" is a key in "table", and the "table"
        # value for said key is not an empty string, then the "plot_countries"
        # key becomes the "output_dict" key and the matched value from "table"
        # becomes the "output_dict" value.
        if (plot_countries[key] in table) and (table[plot_countries[key]] != \
        ''):
            output_dict[key] = table[plot_countries[key]]
        # If the "table" value for said key is an empty string then it moves to
        # "output_set2".
        elif (plot_countries[key] in table) and (table[plot_countries[key]] == \
        ''):
            output_set2.add(key)
        else:
            output_set1.add(key)

    # Convert each value from "output_dict" into it's log base 10.
    for each in output_dict:
        output_dict[each] = math.log(int(output_dict[each]), 10)

    return output_dict, output_set1, output_set2




def render_world_map(gdpinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for
      map_file       - Name of output file to create

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data for the given year and
      writes it to a file named by map_file.
    """
    return


def test_render_world_map():
    """
    Test the project code for several years.
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, pygal_countries, "1960", "isp_gdp_world_name_1960.svg")

    # 1980
    render_world_map(gdpinfo, pygal_countries, "1980", "isp_gdp_world_name_1980.svg")

    # 2000
    render_world_map(gdpinfo, pygal_countries, "2000", "isp_gdp_world_name_2000.svg")

    # 2010
    render_world_map(gdpinfo, pygal_countries, "2010", "isp_gdp_world_name_2010.svg")


# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

# test_render_world_map()
