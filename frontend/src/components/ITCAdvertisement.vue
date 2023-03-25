
<template>
  <div class="itc-advertisement">
    <small class="itc-advertisement__title">This is advertisement</small>
    <div class="itc-advertisement__banner">

    </div>
  </div>
</template>

<style lang="scss" scoped>
.itc-advertisement {
  &__title {
    text-align: center;
    display: block;
    margin: 0 0 10px 0;
  }

  &__banner {
    aspect-ratio: 970 / 250;
    background-color: var(--gray-3);
    width: 100%;
    max-width: 970px;
    margin: 0 auto;
  }
}
</style>
