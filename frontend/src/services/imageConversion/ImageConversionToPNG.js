import axios from 'axios'
import ImageConversionInterface from './ImageConversionInterface.js';

export default class ImageConversionToPNG extends ImageConversionInterface {
    constructor(file, id) {
        super();
        this.id = id;
        this.fileNameBefore = file.name;
        this.fileNameAfter = file.name.replace(/\.(jpg|jpeg|png|gif)$/ig, '.png');
        this.file = file;
        this.complete = false;
        this.error = false;
        this.result = "";
    }

    async convert() {
        const formData = new FormData();
        formData.append("image", this.file);

        try {
            const result = await axios.post('http://localhost:8004/convert/to-png', formData, {
                'Content-Type': 'multipart/form-data'
            }); 

            if (result.status < 200 && result.status >= 300) {
                this.error = true;
                throw new Error("[ImageConversionToPNG, convert]: Something happened to server. Please check backend code. Status " + result.status);
            }

            this.result = result.data;
            this.complete = true;
        } catch(e) {
            this.error = true;
            throw new Error("[ImageConversionToJPG, convert]: Something happened to server. " + e);
        }
    }
}
