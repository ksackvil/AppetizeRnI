import * as React from 'react';
import { Platform, StyleSheet, Text, View } from 'react-native';
import MainScreen from './screens/MainScreen';
import {getItems} from './requests';

export default class App extends React.Component {
  constructor() {
    super();

    this.state = {};
  }

  componentDidMount() {
    getItems()
    .then(res => {
      
    })
    this.setState({test:'1'})
  }

  render() {
    return (
      <View style={styles.container}>
        <MainScreen data={this.state}/>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  instructions: {
    textAlign: 'center',
    color: '#333333',
    marginBottom: 5,
  },
});
