import matplotlib.pyplot as plt
from load_csv import load


def main():
    try:
        data = load("life_expectancy_years.csv")
        if data is None:
            return
        country = "Czech Republic"
        if country not in data['country'].values:
            print(f"{country} not found in the dataset")
            return
        country_data = data[data['country'] == country]
        years = [int(year) for year in data.columns[1:] if str(year).isdigit()]
        life_expectancy = country_data.iloc[0, 1:].values

        plt.plot(years, life_expectancy, label=country)
        plt.title(f"{country} Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.legend()
        plt.show()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
