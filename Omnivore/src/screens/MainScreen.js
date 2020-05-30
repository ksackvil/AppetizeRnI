import * as React from 'react';
import {Text, View } from 'react-native';

class MainScreen extends React.Component {
    constructor(props) {
        super(props);
        console.log(this.props);
        
    }

    render() {
        return(
            <View>
                <Text>hello {this.props.data.test}</Text>
            </View>
        );
    }
}

export default MainScreen;