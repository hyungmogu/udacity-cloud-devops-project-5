import ImageConverterFactory from './imageConverterFactory.js';

export default class ConcreteImageConversionToWEBP extends ImageConverterFactory {
    createTask(file) {
        return ImageConversionToWEBP(
            file.name,
            file
        ) 
    }
}