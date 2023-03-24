<script setup>
import ITCAdvertisement from '../components/ITCAdvertisement.vue'
import ITCHeader from '../components/ITCHeader.vue'
import ITCConvertTool from '../components/ITCConvertTool.vue'
</script>

<template>
  <aside>
    <ITCAdvertisement direction="vertical"/>
  </aside>
  <main>
    <ITCConvertTool/>
  </main>
  <aside>
    <ITCAdvertisement direction="vertical"/>
  </aside>
</template>
