import { FETCH_ANIMALS } from "../actions/types";

const initialState = {
  animals: []
};

export default function(state = initialState, action) {
  console.log("reducer animal:", action.type);
  switch (action.type) {
    case FETCH_ANIMALS:
      return {
        ...state,
        animals: action.payload
      };
    default:
      return state;
  }
}
