import React, { Component } from "react";
import { Provider } from "react-redux";
import AnimalList from "./components/AnimalList";
import RobotList from "./components/RobotList";
import store from "./store/index";

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <div>
          <RobotList />
          <AnimalList />
        </div>
      </Provider>
    );
  }
}

export default App;
