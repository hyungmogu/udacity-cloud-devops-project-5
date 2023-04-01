import axios from 'axios'
import ImageConversionInterface from './imageConversionInterface.js';

export default class ImageConversionToJPG extends ImageConversionInterface {
    constructor(file) {
        super();
        this.fileNameBefore = file.name;
        this.fileNameAfter = file.name.replace(/\.(jpg|jpeg|png|gif)$/ig, '.jpg');
        this.file = file;
        this.complete = false;
        this.error = false;
        this.result = "";
    }
    async convert() {
        const formData = new FormData();
        formData.append("image", this.file);
        try {
            const result = await axios.post('http://localhost:8000/api/convert-to-jpg', formData, {
                'Content-Type': 'multipart/form-data'
            }); 
    
            if (result.status >= 400) {
                this.error = true;
                throw new Error("[ImageConversionToJPG, convert]: Something happened to server. Please check backend code. Status " + result.status);
            }
        
            this.result = result.data;
            this.complete = true;
        } catch(e) {
            this.error = true;
            throw new Error("[ImageConversionToJPG, convert]: Something happened to server. " + e);
        }
    }
}