def model(dbt, session):
    dbt.config(
        packages = ["pandas"]
    )
    import pandas

    data = pandas.read_csv('https://data.seattle.gov/resource/65db-xm6k.csv')
    df = pandas.DataFrame(data)
    return df