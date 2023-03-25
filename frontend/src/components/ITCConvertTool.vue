<script setup>
import ITCButton from "./ITCButton.vue";
import ITCProgressMeter from "./ITCProgressMeter.vue";
</script>

<template>
  <div class="itc-convert-tool">
    <form class="itc-convert-tool__form form">
      <div class="form__group form__group--file">
        <label>Add image files here (.jpg, .jpeg, .png, .svg, .webp only):</label>
        <input type="file" name="file" accept=".jpg, .jpeg, .png, .svg, .webp" multiple/>
      </div>
      <fieldset class="form__fieldset">
        <legend>Select format to convert to:</legend>
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
      <ITCButton :className='"form__button"'>Convert</ITCButton>
    </form>
  </div>
  <div class="itc-convert-tool-result">
    <h2>Result</h2>
    <article class="itc-convert-tool-result__item" v-for="item in 5" :key="item">
      <div class="itc-convert-tool-result__item-wrap">
        <div class="itc-convert-tool-result__item-header">
          <h3 class="itc-convert-tool-result__item-title">Name goes here</h3>
        </div>
        <div class="itc-convert-tool-result__item-body">
          <div class="itc-convert-tool-result__item-progress">
            <ITCProgressMeter/> 
          </div>
          <ITCButton :className='"itc-convert-tool-result__item-download"'>Download</ITCButton>
        </div>
      </div>
    </article>
  </div>
</template>

<style lang="scss" scoped>
.itc-convert-tool {
  margin: 0 0 60px 0;
}

.itc-convert-tool-result {
  &__item-wrap {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  &__item-body {
    display: flex;
    align-items: center;
    & > * {
      &:not(:last-child) {
        margin: 0 30px 0 0;
      }
    }
  }

  &__item {
    margin: 0 0 30px 0;
  }

  &__item-title {
    margin: 0;
    font-weight: var(--font-weight-normal);
    font-size: var(--h6-font-size-mobile);

    @media screen and (min-width: 992px) {
      font-size: var(--h6-font-size);
    }
  }
}
</style>
