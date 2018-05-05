import { FETCH_ROBOTS } from "../actions/types";

const initialState = {
  robots: []
};

export default function(state = initialState, action) {
  console.log("reducer robot:", action.type);
  switch (action.type) {
    case FETCH_ROBOTS:
      return {
        ...state,
        robots: action.payload
      };
    default:
      return state;
  }
}
