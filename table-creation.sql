CREATE TABLE "vaccines" (
    "Country" VARCHAR(100),
    "Alpha-2 code" VARCHAR(10),
    "Alpha-3 code" VARCHAR(10),
    "Numeric code" FLOAT,
    "Latitude" Decimal(8,6),
    "Longitude" Decimal(9,6),
    "WHO_REGION" VARCHAR(5),
    "DATA_SOURCE" VARCHAR(20),
    "DATE_UPDATED" DATE,
    "TOTAL_VACCINATIONS" FLOAT,
    "PERSONS_VACCINATED_1PLUS_DOSE" FLOAT,
    "TOTAL_VACCINATIONS_PER100" FLOAT,
    "PERSONS_VACCINATED_1PLUS_DOSE_PER100" FLOAT,
    "PERSONS_FULLY_VACCINATED" FLOAT,
    "PERSONS_FULLY_VACCINATED_PER100" FLOAT,
    "VACCINES_USED" VARCHAR(1000),
    "FIRST_VACCINE_DATE" DATE,
    "NUMBER_VACCINES_TYPES_USED" FLOAT
);

CREATE TABLE "cases" (
    "Country" VARCHAR(100),
    "Alpha-2 code" VARCHAR(10),
    "Alpha-3 code" VARCHAR(10),
    "Numeric code" FLOAT,
    "Latitude" Decimal(8,6),
    "Longitude" Decimal(9,6),
    "Date_reported" DATE,
    "WHO_region" VARCHAR(5),
    "New_cases" FLOAT,
    "Cumulative_cases" FLOAT,
    "New_deaths" FLOAT,
    "Cumulative_deaths" FLOAT
);


