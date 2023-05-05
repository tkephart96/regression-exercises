# Regression Exercises

Practice regression machine learning using the Zillow dataset on 2017 properties of three CA counties

I acquired the data from the Codeup MySQL DB

Grabbed 7 columns filtered by 'Single Family Residential': bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, and fips

Size was more 2.1 million rows, nulls accounted for less than 1% so I dropped those for now

Renamed columns

Mapped FIPS to county names

## Data Dictionary

| Original                     | Feature    | Type    | Values              | Definition                                               |
| :--------------------------- | :--------- | :------ | :------------------ | :------------------------------------------------------- |
| yearbuilt                    | year       | Year    | 1801-2016           | The year the principal residence was built               |
| bedroomcnt                   | beds       | Numeric | 0-25                | Number of bedrooms in home                               |
| bathroomcnt                  | baths      | Numeric | 0-32                | Number of bathrooms in home including fractional         |
| calculatedfinishedsquarefeet | sqft       | SqFt    | 1~1mil              | Calculated total finished living area                    |
| taxvaluedollarcnt            | total_tax  | USD     | 1~98mil             | The total tax assessed value of the parcel/home          |
| taxamount                    | recent_tax | USD     | 1.85~1.3mil         | The total property tax assessed for that assessment year |
| fips                         | county     | County  | LA, Orange, Ventura | Federal Information Processing Standard (these 3 in CA)  |

FIPS County Codes:

* 06037 = LA County, CA
* 06059 = Orange County, CA
* 06111 = Ventura County, CA

Might turn FIPS to string for encoding later since it is not continuous, it is more of a category
