<template>
    <div class="itc-button" :class="class">
        <a :href="href" :download="download" class="itc-button__button" :disabled="disabled">
            <slot></slot>
        </a>
    </div>
</template>
<script>
export default {
  props:{
    download: {
        type: String,
        default: ''
    },
    href: {
      type: String,
      default: ''  
    },
    class:{
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