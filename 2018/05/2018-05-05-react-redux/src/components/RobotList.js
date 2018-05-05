import React, { Component } from "react";
import { connect } from "react-redux";
import { fetchRobots } from "../actions/robot-actions";

const mapStateToProps = state => {
  // RUNS 1st and last
  console.log("robot: map state to props", state);
  return { x: 1 };
};

class RobotList extends Component {
  constructor(props) {
    // RUNS 2nd
    super(props);
    console.log("robot: constructor props:", props);
  }

  componentWillMount() {
    // RUNS 3rd
    console.log("robot: component mounting");
    this.props.fetchRobots();
  }

  render() {
    // RUNS 4th
    console.log("robot: render");
    return <h1>hello robot list</h1>;
  }
}

export default connect(mapStateToProps, { fetchRobots })(RobotList);
