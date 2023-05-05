# Regression Exercises

Practice regression machine learning using the Zillow dataset on 2017 properties of three CA counties

I acquired the data from the Codeup MySQL DB

Grabbed 7 columns filtered by 'Single Family Residential': bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, and fips

Size was more 2.1 million rows, nulls accounted for less than 1% so I dropped those

## Data Dictionary

| Feature                      | Type         | Values              | Definition                                               |
| :--------------------------- | ------------ | ------------------- | :------------------------------------------------------- |
| bedroomcnt                   | Numeric      | 0-25                | Number of bedrooms in home                               |
| bathroomcnt                  | Numeric      | 0-32                | Number of bathrooms in home including fractional         |
| calculatedfinishedsquarefeet | SqFt         | 1~1mil              | Calculated total finished living area                    |
| taxvaluedollarcnt            | USD          | 1~98mil             | The total tax assessed value of the parcel/home          |
| yearbuilt                    | Year         | 1801-2016           | The year the principal residence was built               |
| taxamount                    | USD          | 1.85~1.3mil         | The total property tax assessed for that assessment year |
| fips                         | 5-Digit Code | 06037, 06059, 06111 | Federal Information Processing Standard (these 3 in CA)  |

FIPS County Codes:
06037 = LA County, CA
06059 = Orange County, CA
06111 = Ventura County, CA

Might turn FIPS to str for encoding later since it is not continuous, it is more of a category


