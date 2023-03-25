<script setup>
import ITCAdvertisement from '../components/ITCAdvertisement.vue'
import ITCHeader from '../components/ITCHeader.vue'
import ITCConvertTool from '../components/ITCConvertTool.vue'
</script>

<template>
  <main>
    <div class="container">
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
  </main>
</template>

<style lang="scss" scoped>
.sidebar-advertisement {

}
</style> 