import matplotlib.pyplot as plt
import numpy as np
from load_csv import load


def convert(string: str) -> float:
    """Convert numbers from string with M and k to float"""
    if string.endswith('M'):
        return float(string[:-1]) * 1000000
    if string.endswith('k'):
        return float(string[:-1]) * 1000
    return float(string)


def main():
    try:
        data = load("population_total.csv")
        if data is None:
            return
        country1 = "Czech Republic"
        country2 = "Germany"

        if country1 not in data['country'].values:
            print(f"{country1} is not in the dataset")
            return
        if country2 not in data['country'].values:
            print(f"{country2} is not in the dataset")
            return

        country1_data = data[data['country'] == country1].iloc[0, 1:].to_dict()
        country2_data = data[data['country'] == country2].iloc[0, 1:].to_dict()

        years = [int(year) for year in data.columns[1:] if
                 str(year).isdigit() and 1800 <= int(year) <= 2050]

        pop1 = []
        pop2 = []
        for year in years:
            try:
                p1 = str(country1_data[str(year)])
                p2 = str(country2_data[str(year)])

                pop1.append(convert(p1))
                pop2.append(convert(p2))
            except Exception:
                pop1.append(None)
                pop2.append(None)

        years_np = np.array(years)
        pop1_np = np.array(pop1, dtype=float)
        pop2_np = np.array(pop2, dtype=float)

        plt.plot(years_np, pop1_np / 1000000, label=country1)
        plt.plot(years_np, pop2_np / 1000000, label=country2)

        formatter = plt.FuncFormatter(lambda x, _: f'{x:.0f}M')
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.yticks(np.arange(20, 100, 20))
        plt.xticks(np.arange(1800, 2050, 40))

        plt.title(f'Population Comparison: {country1} vs {country2}'
                  ' (1800-2050)')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.legend()
        plt.show()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
