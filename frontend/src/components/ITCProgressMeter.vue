<template>
    <div class="itc-progress-meter" v-bind:class="className">
        <span class="itc-progress-meter__bar"></span>
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
@keyframes move {
  0% {
    background-position: 0 0;
  }
  100% {
    background-position: 20px 20px;
  }
}
.itc-progress-meter {
    height: 20px;
    background-color: var(--gray-2);
    border-radius: 25px;
    padding: 5px;
    width: 200px;
    box-shadow: inset 0 -1px 1px rgba(255, 255, 255, 0.3);

    &__bar {
        display: block;
        height: 100%;
        max-width: 100%;
        border-radius: 20px;
        background-color: var(--secondary);
        position: relative;
        box-shadow: inset 0 2px 9px rgba(255, 255, 255, 0.3), inset 0 -2px 6px rgba(0, 0, 0, 0.4);        
        overflow: hidden;

        &::after {
            content: "";
            position: absolute;
            width: 100%;
            height: 100%;
            background-size: 20px 20px;
            background-image: linear-gradient( -45deg, rgba(255, 255, 255, 0.2) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.2) 50%, rgba(255, 255, 255, 0.2) 75%, transparent 75%, transparent );
            animation: move 2s linear infinite;
        }
    }

    &.complete &__bar {
      background-color: var(--third);
      &::after {
        background-image: none;
        animation: none;
      }
    }
}
</style>

