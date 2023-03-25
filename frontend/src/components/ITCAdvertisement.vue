
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
    aspect-ratio: 728 / 90;
    background-color: var(--gray-3);
    width: 100%;
    max-width: 728px;
  }
}
</style>
