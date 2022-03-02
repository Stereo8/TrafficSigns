<script setup lang="ts">
import PitanjeVue from "@/components/Pitanje.vue";
import { getRandId, apiUrl } from "@/util";
import { Suspense, ref, computed, watch } from "vue";
import { NSpin, NProgress } from "naive-ui";
import { useStore } from "@/stores/appState";

const idPitanja = ref(getRandId().toString());

const store = useStore();

const tajmer = ref(90);
const expandTacni = ref(false);
const expandNetacni = ref(false);

const urlPitanja = computed(() => apiUrl + idPitanja.value);
function tacanHandler() {
  expandTacni.value = true;
  setTimeout(() => {
    expandTacni.value = false;
  }, 1000);
  store.brTacnih++;
  if (store.brTacnih == 0) store.brPoena += 100;
  else store.brPoena += (100 * (2 * store.brTacnih - store.brNetacnih)) / 2;
  idPitanja.value = getRandId().toString();
}

function netacanHandler() {
  expandNetacni.value = true;
  setTimeout(() => {
    expandNetacni.value = false;
  }, 1000);
  store.brNetacnih++;
  if (store.brTacnih == 0) store.brPoena -= 100;
  else store.brPoena -= (100 * (2 * store.brTacnih - store.brNetacnih)) / 2;
  if (store.brPoena < 0) store.brPoena = 0;
  idPitanja.value = getRandId().toString();
}

watch(
  tajmer,
  (novi, stari) => {
    if (novi <= 0) {
      store.stanje = "kraj";
    }
    setTimeout(() => {
      tajmer.value = tajmer.value - 1;
    }, 1000);
  },
  { immediate: true }
);
</script>

<template>
  <div class="parent">
    <div
      :class="{
        brTacnih: true,
        expand: expandTacni,
      }"
    >
      {{ store.brTacnih }}
    </div>
    <div
      :class="{
        brNetacnih: true,
        expand: expandNetacni,
      }"
    >
      {{ store.brNetacnih }}
    </div>
    <div class="pitanjeContainer">
      <Suspense>
        <template #default>
          <PitanjeVue
            :url-pitanja="urlPitanja"
            @tacan="tacanHandler"
            @netacan="netacanHandler"
          ></PitanjeVue>
        </template>

        <template #fallback>
          <NSpin size="large" id="vrti"></NSpin>
        </template>
      </Suspense>
    </div>
    <div class="brPoena">{{ store.brPoena }}</div>
    <div class="tajmer">
      <NProgress
        type="line"
        color="#18a058"
        :percentage="tajmer / 1.8"
        unit=""
        :height="24"
        :show-indicator="false"
      ></NProgress>
    </div>
    <div class="rekl1"></div>
    <div class="rekl2"></div>
  </div>
</template>

<style>
.expand {
  animation-name: expand;
  animation-duration: 0.8s;
}

@keyframes expand {
  0% {
    scale: 1;
  }
  50% {
    scale: 4;
  }

  100% {
    scale: 1;
  }
}

.parent {
  background-color: rgba(255, 255, 255, 0.9);
  width: 100%;
  display: grid;
  grid-template-columns: 0.3fr 1fr 0.3fr;
  grid-template-rows: 0.2fr 1fr 0.1fr;
  grid-column-gap: 3px;
  grid-row-gap: 3px;
  align-items: center;
  justify-content: center;
}

.div1 {
  grid-area: 1 / 1 / 2 / 2;
}
.brTacnih {
  grid-area: 1 / 1 / 2 / 2;
  color: green;
  text-align: center;
  font-weight: bolder;
  font-size: large;
}
.brNetacnih {
  grid-area: 1 / 3 / 2 / 4;
  color: crimson;
  text-align: center;
  font-weight: bolder;
  font-size: large;
}
.pitanjeContainer {
  background-color: rgba(255, 255, 255, 0.9);
  grid-area: 2 / 2 / 3 / 3;
  display: flex;
  justify-content: center;
}
.brPoena {
  color: black;
  grid-area: 1 / 2 / 2 / 3;
  text-align: center;
}
.tajmer {
  grid-area: 3 / 1 / 4 / 4;
  text-align: center;
  padding: 1rem;
}
/* .rekl1 {
  grid-area: 2 / 1 / 3 / 2;
}
.rekl2 {
  grid-area: 2 / 3 / 3 / 4;
} */
</style>
