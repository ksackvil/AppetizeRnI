import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import {Subscribe, Provider} from 'unstated-typescript';
import AppCont from './containers/AppCont';

export default function App() {
  return (
    <Provider>
      <Subscribe to={[AppCont]}>
        { cont => (
            <View style={styles.container}>
              <Text>{cont.state.count}</Text>
            </View>
          )
        }
      </Subscribe>
    </Provider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
