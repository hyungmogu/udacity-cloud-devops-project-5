<template>
    <div class="itc-button" v-bind:class="className">
        <button class="itc-button__button" v-bind:disabled="disabled">
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
    },
    disabled: {
     type: Boolean,
     default: false
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
        text-decoration: none;
        display: inline-block;
        font-size: var(--font-size-sm);


        &[disabled] {
            cursor:not-allowed;
            background-color: var(--primary-1);
        }

        &:hover:not([disabled]) {
            background-color: var(--primary-6);
        }
    }
}
</style>