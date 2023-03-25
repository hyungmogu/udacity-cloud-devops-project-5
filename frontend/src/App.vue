<script setup>
import { RouterLink, RouterView } from 'vue-router'
import ITCAdvertisement from './components/ITCAdvertisement.vue'
import ITCHeader from './components/ITCHeader.vue'
</script>

<template>
  <ITCAdvertisement direction="horizontal"/>
  <ITCHeader/>
  <RouterView />
</template>

<style scoped>

</style>
