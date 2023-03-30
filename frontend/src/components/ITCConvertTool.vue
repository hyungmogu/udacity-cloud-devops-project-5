<script setup>
import ITCButton from "./ITCButton.vue";
import ITCProgressMeter from "./ITCProgressMeter.vue";
</script>

<template>
  <div class="itc-convert-tool">
    <form class="itc-convert-tool__form form">
      <div class="form__group form__group--file">
        <label>&#9312; Add image files here (.jpg, .jpeg, .png, .svg, .webp only):</label>
        <ITCButton :className='"form__button form__button--file"'>
          <svg class="form__button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.3.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path fill="currentColor" d="M288 109.3V352c0 17.7-14.3 32-32 32s-32-14.3-32-32V109.3l-73.4 73.4c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3l128-128c12.5-12.5 32.8-12.5 45.3 0l128 128c12.5 12.5 12.5 32.8 0 45.3s-32.8 12.5-45.3 0L288 109.3zM64 352H192c0 35.3 28.7 64 64 64s64-28.7 64-64H448c35.3 0 64 28.7 64 64v32c0 35.3-28.7 64-64 64H64c-35.3 0-64-28.7-64-64V416c0-35.3 28.7-64 64-64zM432 456a24 24 0 1 0 0-48 24 24 0 1 0 0 48z"/></svg>
          <span>Upload Images</span>
        </ITCButton>
        <input ref="images" type="file" name="file" accept=".jpg, .jpeg, .png, .svg, .webp" multiple/>
        <small class="form__annotation form__annotation--info">Files Selected:</small>
      </div>
      <fieldset class="form__fieldset">
        <legend>&#9313; Select format to convert to:</legend>
        <div class="form__group form__group--radio">
          <input type="radio" name="convert_to" value="JPG"/>
          <label>JPG</label>
        </div>
        <div class="form__group form__group--radio">
          <input type="radio" name="convert_to" value="PNG"/>
          <label>PNG</label>
        </div>
        <div class="form__group form__group--radio">
          <input type="radio" name="convert_to" value="WEBP"/>
          <label>WEBP</label>
        </div>
      </fieldset>
      <ITCButton :className='"form__button form__button--submit"'>&#9314; Convert!</ITCButton>
    </form>
    <div class="itc-convert-tool__result">
      <h2>Result</h2>
      <article class="itc-convert-tool__result-item" v-for="item in 5" :key="item">
        <div class="itc-convert-tool__result-item-wrap">
          <div class="itc-convert-tool__result-item-header">
            <h3 class="itc-convert-tool__result-item-title">
              <span class="itc-convert-tool__result-item-before">
                <strong>Before:</strong> <span>before.jpg</span>
              </span>
              <span class="itc-convert-tool__result-item-after">
                <strong>After:</strong> <span>after.png</span>
              </span>
            </h3>
          </div>
          <div class="itc-convert-tool__result-item-body">
            <div class="itc-convert-tool__result-item-progress">
              <ITCProgressMeter/> 
            </div>
            <ITCButton :className='"itc-convert-tool__result-item-download"'>Download</ITCButton>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  data() {
    return {
      tasks: []
    }
  },
  methods: {
    async handleSubmitTasks() {
      for (const taskItem of this.tasks) {
        this.posts = await axios.post('https://localhost:8000/api/convert-to-jpg')
      }
    },
    handleAddTasks() {
      // from factory, generate convert to image task

      // add the task to this.tasks
      for (const file of this.$refs.images.files) {
        console.log(`${file.name}`);
      }
    },
    convertImage() {
      this.handleAddTasks();
      this.handleSubmitTasks();
    }
  }
}
</script>
<style lang="scss" scoped>
.itc-convert-tool {
  &__form {
    margin: 0 0 60px 0;
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
