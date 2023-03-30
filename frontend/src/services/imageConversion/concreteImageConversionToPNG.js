import ImageConverterFactory from './imageConverterFactory.js';
import ImageConversionToPNG from './ImageConversionToPNG.js';

export default class ConcreteImageConversionToPNG extends ImageConverterFactory {
    createTask(file) {
        return ImageConversionToPNG(file) 
    }
}