<script setup lang="ts">
import { NButton } from "naive-ui";
import { ref, defineEmits } from "vue";
import { useStore } from "@/stores/appState";

const store = useStore();
</script>

<template>
  <div class="container">
    <div class="start-screen">
      <div class="welcome-text">
        <h1>Saobraćajni znaci</h1>
      </div>
      <div>
        <NButton @click="store.stanje = 'igra'" class="enter-button"
          >Započni igru</NButton
        >
      </div>
    </div>
  </div>
</template>

<style>
.container {
  width: 100%;
  text-align: center;
  margin-top: 5rem;
}
.welcome-text {
  display: inline-block;
  margin: auto;
}
.enter-button {
  margin-top: 3rem;
  padding: 2rem;
}
</style>
