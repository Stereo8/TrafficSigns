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
        <h1>Saobraćajni znakovi</h1>
      </div>
      <div>
        <NButton @click="store.stanje = 'igra'" class="enter-button1"
          ><h1>TEST 1</h1></NButton
        >
        <NButton @click="store.stanje = 'igra'" class="enter-button2"
          ><h1>TEST 2</h1></NButton
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
  display: grid; 
  grid-template-columns: max-content 1.2fr 1.2fr max-content; 
  grid-template-rows: max-content 1.2fr 1.2fr max-content;
  gap: 6em 0em; 
  grid-template-areas: 
    ". . . ."
    ". welcome-text welcome-text ."
    ". enter-button1 enter-button2 ."
    ". . . ."; 
  justify-items: center; 
}
.welcome-text {
  display: inline-block;
  margin: auto;
  background: rgb(212,0,0);
  background: linear-gradient(90deg, rgba(212,0,0,1) 0%, rgba(203,24,18,0.1600841020001751) 56%, rgba(0,26,255,1) 100%);
  border:2px solid #ffffff;
  color: #ffffff;
  border-radius:10px;
  padding: 10px 15px;

}
.enter-button1, .enter-button2 {
  margin-top: 3rem;
  margin-right: 2rem;
  margin-left: 2rem;
  padding: 2rem;
  background: linear-gradient(90deg, rgba(212,0,0,1) 0%, rgba(203,24,18,0.1600841020001751) 56%, rgba(0,26,255,1) 100%);
  border:2px solid #ffffff;
  color: #ffffff;
  border-radius:10px;
  padding: 25px;
}
</style>
