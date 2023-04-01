import axios from 'axios'
import ImageConversionInterface from './ImageConversionInterface.js';

export default class ImageConversionToWEBP extends ImageConversionInterface {
    constructor(file) {
        super();
        this.fileNameBefore = file.name;
        this.fileNameAfter = file.name.replace(/\.(jpg|jpeg|png|gif)$/ig, '.webp');
        this.file = file;
        this.complete = false;
        this.result = "";
    }
    async convert() {
        const formData = new FormData();
        formData.append("image", this.file);
        const result = await axios.post('http://localhost:8000/api/convert-to-webp', formData, {
            'Content-Type': 'multipart/form-data'
        }); 

        if (result.status !== 200) {
            throw new Error("[ImageConversionToWEBP, convert]: Something happened to server. Please check backend code. Status " + result.status);
        }

        this.result = result.data;
    }
}