<script setup>
import ITCAdvertisement from '../components/ITCAdvertisement.vue'
import ITCHeader from '../components/ITCHeader.vue'
import ITCConvertTool from '../components/ITCConvertTool.vue'
</script>

<template>
  <main class="page">
    <div class="container">
      <div class="page__wrapper">
        <aside class="sidebar-advertisement sidebar-advertisement--left">
          <ITCAdvertisement direction="vertical"/>
        </aside>
        <section>
          <ITCConvertTool/>
        </section>
        <aside class="sidebar-advertisement sidebar-advertisement--right">
          <ITCAdvertisement direction="vertical"/>
        </aside>
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