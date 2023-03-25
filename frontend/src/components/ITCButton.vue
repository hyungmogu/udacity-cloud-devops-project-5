<template>
    <div class="itc-button" v-bind:class="className">
        <button class="itc-button__button">
            <slot></slot>
        </button>
    </div>
</template>
<script>
export default {
  props:{
    className:{
      type:String,
      default:'',
     }
  }
};
</script>
<style lang="scss" scoped>
.itc-button {
    &__button {
        padding: 10px 25px;
        cursor: pointer;
        border: none;
        background-color: var(--primary);
        color: var(--white);
        transition: var(--transition-200);

        &:hover {
            background-color: var(--primary-6);
        }
    }
}
</style>