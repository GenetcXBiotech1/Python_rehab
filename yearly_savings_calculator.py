# --- Display a greeting ---
## Store a greeting in greeting variable
greeting = "Hello "
## Store the name of user
name = "Johnathan"
## Display the concatentation of two strings
print(greeting + name)

# --- Calculate the yearly income ---

## Amount of money usr makes per 1 hour
hourly_wage = 15.5

## Amount of hours worked per 1 week
hours_per_week = 45

## Amount of money made per 1 week
income_per_week = hourly_wage * hours_per_week

## Amount of weeks usr worked per 1 year
weeks_per_year = 46

## Gross amount money made per year
income_per_year = weeks_per_year * income_per_week

## Displaying usr's yearly income
print(name + "'s yearly income is:")
print(income_per_year)

# --- Calculate the yearly spend ---


## Amount usr spent per week
spend_per_week = 400

## Amount usr spent per year
spend_per_year = spend_per_week * 52

## Displaying the amount of money usr spent per year
print(name + "'s yearly spend is:")
print(spend_per_year)


# --- Calculate the yearly savings ---
savings_per_year = income_per_year - spend_per_year
print(name + "'s yearly savings:")
print(savings_per_year)