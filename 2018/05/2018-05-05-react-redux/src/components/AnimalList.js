import React, { Component } from "react";
import { connect } from "react-redux";
import { fetchAnimals } from "../actions/animal-actions";

const mapStateToProps = state => {
  // RUNS 1st and last
  console.log("animal: map state to props", state);
  return { y: 2 };
};

class AnimalList extends Component {
  constructor(props) {
    // RUNS 2nd
    super(props);
    console.log("animal: constructor props:", props);
  }

  componentWillMount() {
    // RUNS 3rd
    console.log("animal: component mounting");
    this.props.fetchAnimals();
  }

  render() {
    // RUNS 4th
    console.log("animal: render");
    return <h1>hello animal list</h1>;
  }
}

export default connect(mapStateToProps, { fetchAnimals })(AnimalList);
