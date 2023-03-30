import ImageConverterFactory from './imageConverterFactory.js';

export default class ConcreteImageConversionToPNG extends ImageConverterFactory {
    createTask(file) {
        return ImageConversionToPNG(
            file.name,
            file
        ) 
    }
}