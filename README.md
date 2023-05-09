# Regression Exercises

Practice regression machine learning using the Zillow dataset on 2017 properties of three CA counties

I acquired the data from the Codeup MySQL DB

Grabbed 7 columns filtered by 'Single Family Residential': bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, and fips

Size was more 2.1 million rows, nulls accounted for less than 1% so I dropped those for now

Renamed columns

Mapped FIPS to county names

Handled outliers by filtering area to less than 25,000 and tax_value to less than its 95th quantile

Dropped properties where beds or baths were 0, accounted for less than 1%

Data after this is now about 2.03 mil rows

I plan to scale year, beds, baths, area, and prop_tax using RobustScaler for now, may switch later

Encoded county to 1s and 0s

## Data Dictionary

| Original                     | Feature    | Type    | Values              | Definition                                               |
| :--------------------------- | :--------- | :------ | :------------------ | :------------------------------------------------------- |
| yearbuilt                    | year       | Year    | 1801-2016           | The year the principal residence was built               |
| bedroomcnt                   | beds       | Numeric | 1-25                | Number of bedrooms in home                               |
| bathroomcnt                  | baths      | Numeric | 0.5-32              | Number of bathrooms in home including fractional         |
| calculatedfinishedsquarefeet | area       | SqFt    | 1~1mil              | Calculated total finished living area                    |
| taxvaluedollarcnt (target)   | prop_value | USD     | 1~98mil             | The total tax assessed value of the parcel/home          |
| taxamount                    | prop_tax   | USD     | 1.85~1.3mil         | The total property tax assessed for that assessment year |
| fips                         | county     | County  | LA, Orange, Ventura | Federal Information Processing Standard (these 3 in CA)  |
| Additional Features          |            | Numeric | 1=True, 0=False     | Encoded categorical variables                            |

FIPS County Codes:

* 06037 = LA County, CA
* 06059 = Orange County, CA
* 06111 = Ventura County, CA
