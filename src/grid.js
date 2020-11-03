// fill in the grid

const gridSizeX = 10;
const gridSizeY = 10;

const createCity = (locationPoint, country) => ({
  balance: 0,
});

const getEmptyGrid = () => {
  return Array(gridSizeY)
    .fill(null)
    .map(() => Array(gridSizeX));
};

// country { name, lowerLeft, upperRight}

export const fillInitialGrid = (countries) => {
  let grid = getEmptyGrid();

  for (let country in countries) {
  }

  return grid;
};
