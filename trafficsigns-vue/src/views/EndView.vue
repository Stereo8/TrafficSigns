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
  background-color: rgba(255, 255, 255, 0.9);
  color: black;
  display: inline-block;
  font-weight: bold;
  font-size: larger;
  margin: auto;
}
.end-stats{
  background-color: rgba(255, 255, 255, 0.9);
  color: black;
}
.restart-button {
  background: rgb(212,0,0);
  background: linear-gradient(90deg, rgba(212,0,0,1) 10%, rgba(203,24,18,0.1600841020001751) 56%, rgba(0,26,255,1) 100%);
  border:2px solid #ffffff;
  color: white;
  border-radius: 10px;
  margin-top: 2rem;
  padding: 2rem 4rem;
}
</style>
