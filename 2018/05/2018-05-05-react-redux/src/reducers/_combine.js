import { combineReducers } from "redux";
import animalReducer from "./animal-reducers";
import robotReducer from "./robot-reducers";

export default combineReducers({
  animalstore: animalReducer,
  robotstore: robotReducer
});
