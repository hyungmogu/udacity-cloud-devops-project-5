<template>
    <div class="itc-button itc-button--link" :class="className">
        <a :href="href" :download="download" :target="target" class="itc-button__button" :disabled="disabled ? disabled : null">
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
    className:{
      type:String,
      default:'',
    },
    target:{
      type:String,
      default:'_self',
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
        padding: 12px 25px;
        cursor: pointer;
        border: none;
        background-color: var(--primary);
        color: var(--white);
        transition: var(--transition-200);
        text-decoration: none;
        display: inline-block;
        font-size: var(--font-size-sm);
        line-height: 1;

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