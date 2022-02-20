<script setup lang="ts">
import { useStore } from "@/stores/appState";
import { NButton } from "naive-ui";

const store = useStore();
</script>

<template>
  <div class="container">
    <div class="end-screen">
      <div class="end-text">
        <h1>Kraj igre!</h1>
      </div>
      <div class="end-stats">
        <div>
          Poeni:
          <p class="poeni">{{ store.brPoena }}</p>
        </div>
        <div>
          Broj tačnih odgovora:
          <p class="tacni">{{ store.brTacnih }}</p>
        </div>
        <div>
          Broj netačnih odgovora:
          <p class="netacni">{{ store.brNetacnih }}</p>
        </div>
      </div>
      <NButton @click="store.$reset()" class="restart-button">Restart</NButton>
    </div>
  </div>
</template>

<style scoped>
.container {
  width: 100%;
  text-align: center;
  margin-top: 5rem;
}
.end-text {
  display: inline-block;
  font-weight: bold;
  font-size: larger;
  margin: auto;
}
.restart-button {
  margin-top: 3rem;
  padding: 2rem;
}
</style>
