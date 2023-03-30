export default class ImageConverterFactory {
    constructor() {
        if (this.constructor == ImageConverterFactory) {
            throw new Error("Abstract class can't be instantiated.");
        }
    }
    createTask() {
        throw new Error("Method 'createTask()' must be implemented.");
    }
}