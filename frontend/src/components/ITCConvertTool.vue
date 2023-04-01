<script setup>
import ITCButton from "./ITCButton.vue";
import ITCProgressMeter from "./ITCProgressMeter.vue";
import ConcreteImageConversionToJPG from '@/services/imageConversion/concreteImageConversionToJPG.js'; 
import ConcreteImageConversionToPNG from '@/services/imageConversion/concreteImageConversionToPNG.js'; 
import ConcreteImageConversionToWEBP from '@/services/imageConversion/concreteImageConversionToWEBP.js'; 
</script>

<template>
  <div class="itc-convert-tool">
    <form class="itc-convert-tool__form form">
      <div class="form__group form__group--file">
        <label>&#9312; Add image files here (.jpg, .jpeg, .png, .svg, .webp only):</label>
        <ITCButton :className='"form__button form__button--file"' @click="selectImages">
          <svg class="form__button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.3.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path fill="currentColor" d="M288 109.3V352c0 17.7-14.3 32-32 32s-32-14.3-32-32V109.3l-73.4 73.4c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3l128-128c12.5-12.5 32.8-12.5 45.3 0l128 128c12.5 12.5 12.5 32.8 0 45.3s-32.8 12.5-45.3 0L288 109.3zM64 352H192c0 35.3 28.7 64 64 64s64-28.7 64-64H448c35.3 0 64 28.7 64 64v32c0 35.3-28.7 64-64 64H64c-35.3 0-64-28.7-64-64V416c0-35.3 28.7-64 64-64zM432 456a24 24 0 1 0 0-48 24 24 0 1 0 0 48z"/></svg>
          <span>Upload Images</span>
        </ITCButton>
        <input ref="images" type="file" name="file" accept=".jpg, .jpeg, .png, .svg, .webp" multiple @change="updateSelected"/>
        <small class="form__annotation form__annotation--info">Files Selected: {{ selectedFiles }}</small>
      </div>
      <fieldset class="form__fieldset">
        <legend>&#9313; Select format to convert to:</legend>
        <div class="form__group form__group--radio">
          <input type="radio" name="convert_to" value="JPG" v-model="form.convert_to"/>
          <label>JPG</label>
        </div>
        <div class="form__group form__group--radio">
          <input type="radio" name="convert_to" value="PNG" v-model="form.convert_to"/>
          <label>PNG</label>
        </div>
        <div class="form__group form__group--radio">
          <input type="radio" name="convert_to" value="WEBP" v-model="form.convert_to"/>
          <label>WEBP</label>
        </div>
      </fieldset>
      <ITCButton :className='"form__button form__button--submit"' @click="convertImage">&#9314; Convert!</ITCButton>
    </form>
    <div class="itc-convert-tool__result">
      <h2 v-if="tasks.length > 0">Result</h2>
      <article class="itc-convert-tool__result-item" v-for="item in tasks">
        <div class="itc-convert-tool__result-item-wrap">
          <div class="itc-convert-tool__result-item-header">
            <h3 class="itc-convert-tool__result-item-title">
              <span class="itc-convert-tool__result-item-before">
                <strong>Before:</strong> <span>{{ item.fileNameBefore }}</span>
              </span>
              <span class="itc-convert-tool__result-item-after">
                <strong>After:</strong> <span>{{ item.fileNameAfter }}</span>
              </span>
            </h3>
          </div>
          <div class="itc-convert-tool__result-item-body">
            <div class="itc-convert-tool__result-item-progress">
              <ITCProgressMeter/> 
            </div>
            <ITCButton :className='"itc-convert-tool__result-item-download"' v-bind:disabled="item.result.trim() === ''">Download</ITCButton>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>
<script>
const defaultForm = {
  images: null,
  convert_to: 'JPG'
}

export default {
  data() {
    return {
      form: {...defaultForm},
      selectedFiles: "",
      tasks: []
    }
  },
  methods: {
    async handleSubmitTasks() {
      for (const taskItem of this.tasks) {
        taskItem.convert();
      }
    },
    handleUpdateListOfImagesAnnotation() {
      this.selectedFiles = [...this.form.images.files].map((item, index) => (index+1) + '. ' + item.name).join(", ");
    },
    handleUpdateImages() {
      this.form.images = this.$refs.images;
    },
    handleAddTasks() {
      for (const file of this.form.images.files) {
        let factory;
        switch (this.form.convert_to) {
          case "JPG":
            factory = new ConcreteImageConversionToJPG();
            break;
          case "PNG":
            factory = new ConcreteImageConversionToPNG();
            break;
          case "WEBP":
            factory = new ConcreteImageConversionToWEBP();
            break;
          default:
            throw new Error("[ITCConvertTool, handleAddTasks]: Image convert to type is invalid. Please check if radio values are correct.");
        }

        this.tasks.push(factory.createTask(file));
      }
    },
    convertImage(e) {
      e.preventDefault();
      this.handleAddTasks();
      this.handleSubmitTasks();
    },
    updateSelected(e) {
      this.handleUpdateImages();
      this.handleUpdateListOfImagesAnnotation();
    },
    selectImages(e) {
      e.preventDefault();
      this.$refs.images.click();
    }
  }
}
</script>
<style lang="scss" scoped>
.itc-convert-tool {
  &__form {
    margin: 0 0 60px 0;
  }

  &__form .form__group--file {
    text-align: center;
    max-width: 470px;
    margin: 0 auto 30px auto;

    @media screen and (min-width: 992px) {
      text-align: left;
      max-width: 100%;
      margin: 0 0 30px 0;
    }
  }

  &__form .form__button--submit {
    text-align: center;

    @media screen and (min-width: 992px) {
      text-align: left;
    }
  }

  &__result-item-wrap {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  &__result-item-body {
    display: flex;
    align-items: center;
    & > * {
      &:not(:last-child) {
        margin: 0 30px 0 0;
      }
    }
  }

  &__result-item {
    margin: 0 0 30px 0;
  }

  &__result-item-title {
    margin: 0;
    font-weight: var(--font-weight-normal);
    font-size: var(--h6-font-size-mobile);

    @media screen and (min-width: 992px) {
      font-size: var(--h6-font-size);
    }

    & > * {
      display: block;

      &:not(:last-child) {
        margin: 0 0 10px 0;
      }
    }
  }

  &__result-item-before strong,
  &__result-item-after strong {
    font-weight: var(--font-weight-bold);
  }
}

</style>
