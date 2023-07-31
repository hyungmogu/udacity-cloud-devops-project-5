import ImageConverterFactory from './imageConverterFactory.js';
import ImageConversionToJPG from './ImageConversionToJPG.js';

export default class ConcreteImageConversionToJPG extends ImageConverterFactory {
    createTask(file, id) {
        return new ImageConversionToJPG(file, id)
    }
}