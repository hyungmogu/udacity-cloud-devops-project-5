<script setup>
import ITCAdvertisement from '../components/ITCAdvertisement.vue'
import ITCPageBanner from '../components/ITCPageBanner.vue'
import ITCConvertTool from '../components/ITCConvertTool.vue'
</script>

<template>
  <main class="page">
    <div class="container">
      <div class="page__wrapper">
        <section>
          <ITCAdvertisement/>
          <ITCPageBanner/>
          <ITCConvertTool/>
          <ITCAdvertisement/>
        </section>
      </div>
    </div>
  </main>
</template>

<style lang="scss" scoped>
.page {
  &__wrapper {
    position: relative;
  }
}
.sidebar-advertisement {
  position: sticky;
  top: 50%;

  &--left {
    transform: translate(calc(-100% + 10px), -50%);
  }

  &--right {
    transform: translate(calc(100% + 10px), -50%);
  }
}
</style> 