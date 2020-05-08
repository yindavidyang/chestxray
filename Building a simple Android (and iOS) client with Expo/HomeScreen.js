import * as React from 'react';
import {Image, Button, Text, View} from 'react-native';

import * as ImagePicker from 'expo-image-picker';
import * as Permissions from 'expo-permissions';

export default class HomeScreen extends React.Component {
    state = {
        image: null,
        prediction: null,
    }

    render() {
        return (
            <View style={{flex: 1, alignItems: 'center', justifyContent: 'center'}}>
                <Button title="Pick an image" onPress={this._pickImage}/>
                <Image source={this.state.image} style={{height: 200, width: 200}}/>
                <Text>Prediction: {this.state.prediction && this.state.prediction.result}</Text>
            </View>
        );
    }

    _pickImage = async () => {
        const {status} = await Permissions.askAsync(Permissions.CAMERA_ROLL);
        if (status !== 'granted') {
            alert(status);
        }

        let result = await ImagePicker.launchImageLibraryAsync();

        if (!result.cancelled) {
            await this._processImage(result);
        } else {
            alert(result);
        }
    };

    _processImage = async (imageData) => {
        this.setState({image: {uri: imageData.uri}});

        let data = new FormData();
        data.append('file', {
            uri: imageData.uri,
            name: `photo.jpeg`,
            type: `image/jpeg`,
        });

        const response = await fetch('https://pneumonia.qspc.qa/analyze', {
            method: 'POST',
            body: data,
            headers: {
                'Content-Type': 'multipart/form-data',
                'Accept': 'application/json'
            }
        })

        const result = await response.json()
        console.log(result)

        this.setState({prediction: result});
    };
}
