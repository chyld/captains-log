import { FETCH_ROBOTS } from "./types";

// json-server -p 3001 --watch server/data.json

export const fetchRobots = () => dispatch => {
  console.log("action: fetch_robots");
  fetch("http://localhost:3001/robots")
    .then(res => res.json())
    .then(robots =>
      dispatch({
        type: FETCH_ROBOTS,
        payload: robots
      })
    );
};
