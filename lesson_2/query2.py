import pandas
import pandasql


def aggregate_query(filename):
    aadhaar_data = pandas.read_csv(filename)
    aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(),
                        inplace=True)

    # Write a query that will select from the aadhaar_data table how
    # many men and how many women over the age of 50 have had
    # aadhaar generated for them in each district
    #
    # The possible columns to select from aadhaar data are:
    #     1) Registrar
    #     2) Enrolment Agency
    #     3) State
    #     4) District
    #     5) Sub District
    #     6) Pin Code
    #     7) Gender
    #     8) Age
    #     9) Aadhaar generated
    #     10) Enrolment Rejected
    #     11) Residents providing email,
    #     12) Residents providing mobile number
    #
    # You can download a copy of the aadhaar data that we are passing
    # into this exercise below:
    # https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv

    q = """
    select gender, district, sum(aadhaar_generated) from aadhaar_data where age > 50 group by gender, district
    """

    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    return aadhaar_solution
