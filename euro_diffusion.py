from src import Map


if __name__ == "__main__":
    # France 1 4 4 6
    # Spain 3 1 6 3
    # Portugal 1 1 2 2
    cases = [[
        {
            "name": "France",
            "ll": {
                "x": 1,
                "y": 4,
            },
            "ur": {
                "x": 4,
                "y": 6,
            }
        },
        {
            "name": "Spain",
            "ll": {
                "x": 3,
                "y": 1,
            },
            "ur": {
                "x": 6,
                "y": 3,
            }
        },
        {
            "name": "Portugal",
            "ll": {
                "x": 1,
                "y": 1,
            },
            "ur": {
                "x": 2,
                "y": 2,
            }
        },
    ]]
    for i, countries_list in enumerate(cases):
        europe_map = Map(countries_list)
        europe_map.simulate_euro_diffusion()

        print("Case Number %i" % (i + 1))
        if europe_map.err is None:
            for country in europe_map.countries:
                print(country.name, country.day_of_full)
        else:
            print(europe_map.err)
