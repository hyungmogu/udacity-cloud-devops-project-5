import axios from 'axios'
import ImageConversionInterface from './ImageConversionInterface.js';

export default class ImageConversionToPNG extends ImageConversionInterface {
    constructor(fileName, file) {
        this.fileName = fileName;
        this.file = file;
        this.complete = false;
        this.link = "";
    }
    convert() {
        return 
    }
}