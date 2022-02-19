<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
import HomeView from "@/views/HomeView.vue";
</script>

<template>
  <RouterView to="/"></RouterView>
</template>

<style>
@import "@/assets/base.css";

#app {
  display: flex;
  place-items: center;
}

@media (hover: hover) {
  a:hover {
    background-color: hsla(160, 100%, 37%, 0.2);
  }
}

@media (min-width: 1024px) {
  body {
    display: flex;
    justify-content: center;
  }
}
</style>
