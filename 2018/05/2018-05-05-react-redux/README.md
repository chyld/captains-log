# react + redux

### run json server

json-server -p 3001 --watch server/data.json

### start node server

npm start

### data flow

* reducer initialization, sending default store to all components
* each component's `mapStateToProps` gets called first
* then each component's `constructor` gets called with the new props from above
* the component mounts and calls the action method that was sent in via props
* the action get called and calls the webservice
* the returned data from the call gets sent to the correct reducer
* all reducers get called, but each reducer filters out who the call actually belongs to
* since all reducers get called, after they are done, all `mapStateToProps` get called in all components

### raw output log

reducer animal: @@redux/INIT8.f.p.e.l.l
animal-reducers.js:8 reducer animal: @@redux/PROBE_UNKNOWN_ACTION_9.c.l.o.l
robot-reducers.js:8 reducer robot: @@redux/INIT8.f.p.e.l.l
robot-reducers.js:8 reducer robot: @@redux/PROBE_UNKNOWN_ACTION_0.0.b.5.x.h
animal-reducers.js:8 reducer animal: @@INIT
robot-reducers.js:8 reducer robot: @@INIT
RobotList.js:7 robot: map state to props {animalstore: {…}, robotstore: {…}}
RobotList.js:15 robot: constructor props: {x: 1, fetchRobots: ƒ}
RobotList.js:20 robot: component mounting
robot-actions.js:6 action: fetch_robots
RobotList.js:26 robot: render
AnimalList.js:7 animal: map state to props {animalstore: {…}, robotstore: {…}}
AnimalList.js:15 animal: constructor props: {y: 2, fetchAnimals: ƒ}
AnimalList.js:20 animal: component mounting
animal-actions.js:6 action: fetch_animals
AnimalList.js:26 animal: render
animal-reducers.js:8 reducer animal: FETCH_ROBOTS
robot-reducers.js:8 reducer robot: FETCH_ROBOTS
RobotList.js:7 robot: map state to props {animalstore: {…}, robotstore: {…}}
AnimalList.js:7 animal: map state to props {animalstore: {…}, robotstore: {…}}
animal-reducers.js:8 reducer animal: FETCH_ANIMALS
robot-reducers.js:8 reducer robot: FETCH_ANIMALS
RobotList.js:7 robot: map state to props {animalstore: {…}, robotstore: {…}}
AnimalList.js:7 animal: map state to props {animalstore: {…}, robotstore: {…}}
