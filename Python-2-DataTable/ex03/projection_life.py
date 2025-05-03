import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from load_csv import load


def main():
    try:
        income_data = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_data = load("life_expectancy_years.csv")

        if income_data is None or life_data is None:
            return

        year = '1900'

        countries = []
        gdp_values = []
        life_expectancy_values = []

        for idx, country in enumerate(income_data['country']):
            if country in life_data['country'].values:
                gdp = income_data.loc[idx, year]
                life_idx = life_data[life_data['country'] == country].index[0]
                life_exp = life_data.loc[life_idx, year]

                if pd.isna(gdp) or pd.isna(life_exp):
                    continue

                try:
                    gdp = float(gdp)
                    life_exp = float(life_exp)

                    countries.append(country)
                    gdp_values.append(gdp)
                    life_expectancy_values.append(life_exp)
                except (ValueError, TypeError):
                    continue

        plt.figure(figsize=(6, 5))

        plt.scatter(gdp_values, life_expectancy_values, label="Countries in 1900")

        plt.title('1900')
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life Expectancy')

        plt.xscale('log')
        plt.xticks([300, 1000, 10000], [300, "1k", "10k"])
        plt.legend()

        plt.show()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")

if __name__ == "__main__":
    main()
