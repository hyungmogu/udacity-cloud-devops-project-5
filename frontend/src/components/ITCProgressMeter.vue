<template>
    <div class="itc-progress-meter">
        <span class="itc-progress-meter__bar"></span>
    </div>
</template>

<style lang="scss" scoped>
@keyframes move {
  0% {
    background-position: 0 0;
  }
  100% {
    background-position: 50px 50px;
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
        max-width: 20%;
        border-top-right-radius: 8px;
        border-bottom-right-radius: 8px;
        border-top-left-radius: 20px;
        border-bottom-left-radius: 20px;
        background-color: var(--secondary);
        position: relative;
        box-shadow: inset 0 2px 9px rgba(255, 255, 255, 0.3), inset 0 -2px 6px rgba(0, 0, 0, 0.4);        overflow: hidden;
    }
}
</style>

