export default class ImageConversionInterface {
    constructor(name, file) {
        if (arguments.length < 2) {
            throw new Error('An Interface expects atleast 2 arguments ' + arguments.length
                + ' arguments passed')
            
        }

        this.name = name;
        this.file = file;
    }

    submit(file) {
        return 
    }
}