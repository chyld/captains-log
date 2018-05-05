import { FETCH_ANIMALS } from "./types";

// json-server -p 3001 --watch server/data.json

export const fetchAnimals = () => dispatch => {
  console.log("action: fetch_animals");
  fetch("http://localhost:3001/animals")
    .then(res => res.json())
    .then(animals =>
      dispatch({
        type: FETCH_ANIMALS,
        payload: animals
      })
    );
};
