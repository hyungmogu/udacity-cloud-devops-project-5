import axios from 'axios'
import ImageConversionInterface from './ImageConversionInterface.js';

export default class ImageConversionToWEBP extends ImageConversionInterface {
    constructor(fileName, file) {
        super();
        this.fileName = fileName;
        this.file = file;
        this.complete = false;
        this.result = "";
    }
    async convert() {
        const result = await axios.post('https://localhost:8000/api/convert-to-webp', {
            image: this.file
        }, {
            'Content-Type': 'multipart/form-data'
        }); 

        if (result.status !== 200) {
            throw new Error("[ImageConversionToWEBP, convert]: Something happened to server. Please check backend code. Status " + result.status);
        }

        this.result = result.data;
    }
}