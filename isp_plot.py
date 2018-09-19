
"""
Project for Week 2 of "Python Data Visualization".
Read World Bank GDP data and create some basic XY plots.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import pygal




def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """

    # Establish output reference.
    table = {}

    # Open argued "filename" as reference "csvfile".
    with open(filename, newline='') as csvfile:
        # With "DictReader" function convert "csvfile" to dictionary as
        # "csvreader".
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)

        # Iterate over "csvreader" to nest argued "keyfield" as columns within
        # rows.
        for row in csvreader:
            rowid = row[keyfield]
            table[rowid] = row

    return table




def build_plot_values(gdpinfo, gdpdata):
    """
    Inputs:
      gdpinfo - GDP data information dictionary
      gdpdata - A single country's GDP stored in a dictionary whose
                keys are strings indicating a year and whose values
                are strings indicating the country's corresponding GDP
                for that year.

    Output:
      Returns a list of tuples of the form (year, GDP) for the years
      between "min_year" and "max_year", inclusive, from gdpinfo that
      exist in gdpdata.  The year will be an integer and the GDP will
      be a float.
    """

    # Establish return reference.
    output = []
    # Lists to be zipped into "output".
    list_year = []
    list_data = []

    # Iteration filters through argued "gdpdata".  Iteration filters in all
    # years between "min_year" and "max_year" in argued dict "gdpinfo".
    # Iteration filters out all argued "gdpdata" values that are empty strings.
    for each in range(gdpinfo['min_year'], gdpinfo['max_year']+1, 1):
        if str(each) in gdpdata and gdpdata[str(each)] != '':
            list_year.append(each)

    # Iteration appends to "list_data" all keys from argued "gdpdata" that
    # correspond to items in "list_year".  All appends are then converted to
    # float.
    for each in list_year:
        list_data.append(float(gdpdata[str(each)]))

    # Convert zipped "output" from a generator to an object list
    output = list(zip(list_year, list_data))

    return output




def build_plot_dict(gdpinfo, country_list):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names

    Output:
      Returns a dictionary whose keys are the country names in
      country_list and whose values are lists of XY plot values
      computed from the CSV file described by gdpinfo.

      Countries from country_list that do not appear in the
      CSV file should still be in the output dictionary, but
      with an empty XY plot value list.
    """

    # Establish output reference.
    output = {}
    # Establish dict reference to call "read_csv_as_nested_dict" function.
    dict_data = {}
    # Establish list reference to call "build_plot_values" function.
    plot_values = []

    # Run "read_csv_as_nested_dict" function on 'gdpfile' in argued "gdpinfo".
    # "dict_data" saves 'gdpfile' as nested dictionaries within 'country_name'
    # in argued "gdpinfo".
    dict_data = read_csv_as_nested_dict(gdpinfo['gdpfile'], \
    gdpinfo['country_name'], gdpinfo['separator'], gdpinfo['quote'])

    # Iterate over argued "country_list" to nest the tupled list created from
    # "build_plot_values" function within each item from "country_list".
    for each in country_list:
        if each in dict_data:
            plot_values = build_plot_values(gdpinfo, dict_data[each])
            output[each] = plot_values
        # "if" / "else" statements are to refer items within "country_list"
        # that are not within argued "gdpinfo['gdpfile']" to an empty list.
        else:
            output[each] = []

    return output




def render_xy_plot(gdpinfo, country_list, plot_file):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names
      plot_file    - String that is the output plot file name

    Output:
      Returns None.

    Action:
      Creates an SVG image of an XY plot for the GDP data
      specified by gdpinfo for the countries in country_list.
      The image will be stored in a file named by plot_file.
    """
    return




def test_render_xy_plot():
    """
    Code to exercise render_xy_plot and generate plots from
    actual GDP data.
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

    render_xy_plot(gdpinfo, [], "isp_gdp_xy_none.svg")
    render_xy_plot(gdpinfo, ["China"], "isp_gdp_xy_china.svg")
    render_xy_plot(gdpinfo, ["United Kingdom", "United States"],
                   "isp_gdp_xy_uk+usa.svg")


# Make sure the following call to test_render_xy_plot is commented out
# when submitting to OwlTest/CourseraTest.

# test_render_xy_plot()
