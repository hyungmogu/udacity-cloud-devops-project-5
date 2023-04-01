import axios from 'axios'
import ImageConversionInterface from './ImageConversionInterface.js';

export default class ImageConversionToPNG extends ImageConversionInterface {
    constructor(file) {
        super();
        this.fileNameBefore = file.name;
        this.fileNameAfter = file.name.replace(/\.(jpg|jpeg|png|gif)$/ig, '.png');
        this.file = file;
        this.complete = false;
        this.result = "";
    }

    async convert() {
        const result = await axios.post('http://localhost:8000/api/convert-to-png', {
            image: this.file
        }, {
            'Content-Type': 'multipart/form-data'
        }); 

        if (result.status !== 200) {
            throw new Error("[ImageConversionToPNG, convert]: Something happened to server. Please check backend code. Status " + result.status);
        }

        this.result = result.data;
    }
}