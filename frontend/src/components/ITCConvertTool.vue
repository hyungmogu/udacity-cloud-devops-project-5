<script setup>
import ITCButton from "./ITCButton.vue";
</script>

<template>
  <div class="itc-convert-tool">
    <form class="itc-convert-tool__form form">
      <div class="form__group form__group--file">
        <label>Add image files here (.jpg, .jpeg, .png, .svg, .webp only):</label>
        <input type="file" name="file" accept=".jpg, .jpeg, .png, .svg, .webp"/>
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
</template>

<style lang="scss" scoped>

</style>
