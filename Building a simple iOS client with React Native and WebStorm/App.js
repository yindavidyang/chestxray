import React from 'react';
import {View, Image, Button} from 'react-native';
import ImagePicker from 'react-native-image-picker';

const createFormData = (photo) => {
    const data = new FormData();

    data.append('file', {
        name: 'image.jpg',
        type: photo.type,
        uri:
            Platform.OS === 'android' ? photo.uri : photo.uri.replace('file://', ''),
    });
    return data;
};

export default class App extends React.Component {
    state = {
        photo: null,
    };

    handleChoosePhoto = () => {
        const options = {
            noData: true,
        };
        ImagePicker.launchImageLibrary(options, (response) => {
            if (response.uri) {
                this.setState({photo: response});
            }
        });
    };

    handleUploadPhoto = () => {
        fetch('https://pneumonia.qspc.qa/analyze', {
            method: 'POST',
            body: createFormData(this.state.photo),
        })
            .then((response) => response.json())
            .then((response) => {
                console.log('upload success', response);
                alert(response['result']);
                this.setState({photo: null});
            })
            .catch((error) => {
                console.log('upload error', error);
                alert('Upload failed!', error);
            });
    };

    render() {
        const {photo} = this.state;
        return (
            <View style={{flex: 1, alignItems: 'center', justifyContent: 'center'}}>
                {photo && (
                    <React.Fragment>
                        <Image
                            source={{uri: photo.uri}}
                            style={{width: 300, height: 300}}
                        />
                        <Button title="Analyze" onPress={this.handleUploadPhoto}/>
                    </React.Fragment>
                )}
                <Button title="Choose chest X-ray image" onPress={this.handleChoosePhoto}/>
            </View>
        );
    }
}
