import ImageConverterFactory from './imageConverterFactory.js';
import ImageConversionToWEBP from './ImageConversionToWEBP.js';

export default class ConcreteImageConversionToWEBP extends ImageConverterFactory {
    createTask(file) {
        return ImageConversionToWEBP(file) 
    }
}