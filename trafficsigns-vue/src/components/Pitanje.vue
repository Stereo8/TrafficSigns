<script setup lang="ts">
import { ref, watch } from "vue";
import { reactive } from "vue";
import { onMounted } from "vue";
import { Transition } from "vue";
import { NButton } from "naive-ui";
import { apiSlikeUrl } from "@/util";

interface Pitanje {
  znak: string;
  opis: string;
  tacan_odg: string;
  netacni_odg1: string;
  netacni_odg2: string;
}

function shuffle(array: any[]) {
  for (let i = array.length - 1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

const props = defineProps({
  urlPitanja: { type: String, required: true },
});

const emit = defineEmits(["tacan", "netacan"]);

let p: Pitanje = await fetch(props.urlPitanja)
  .then((response) => response.json())
  .then((data) => data);

const pitanje = ref(p);
const shaking = ref(false);
const colorG = ref(false);

const listaOdgovora = ref([
  { tekst: pitanje.value.tacan_odg, tacan: true },
  { tekst: pitanje.value.netacni_odg1, tacan: false },
  { tekst: pitanje.value.netacni_odg2, tacan: false },
]);

function checkOdgovor(tacnost: boolean, event: Event) {
  if (tacnost) {
    emit("tacan");
  } else {
    protresi();
    obojZeleno();
    setTimeout(() => {
      emit("netacan");
    }, 1000);
  }
}

function obojZeleno() {
  colorG.value = true;
  setTimeout(() => (colorG.value = false), 800);
}

function protresi() {
  shaking.value = true;
  setTimeout(() => {
    shaking.value = false;
  }, 850);
}

shuffle(listaOdgovora.value);

console.log(listaOdgovora.value);

watch(
  () => props.urlPitanja,
  async (novi, stari) => {
    pitanje.value = await fetch(novi)
      .then((response) => response.json())
      .then((data) => data);

    listaOdgovora.value = [
      { tekst: pitanje.value.tacan_odg, tacan: true },
      { tekst: pitanje.value.netacni_odg1, tacan: false },
      { tekst: pitanje.value.netacni_odg2, tacan: false },
    ];
    shuffle(listaOdgovora.value);
  }
);
</script>

<template>
  <div class="pitanje">
    <div class="slikaPitanja">
      <img
        :class="{ shake: shaking }"
        :src="apiSlikeUrl + pitanje.znak"
        :alt="pitanje.tacan_odg"
        :key="pitanje.znak"
      />
    </div>

    <section class="odgovori">
      <template v-for="odgovor in listaOdgovora">
        <NButton
          :class="{ colorGreen: colorG && odgovor.tacan, dugme: true }"
          @click="checkOdgovor(odgovor.tacan, $event)"
          :focusable="false"
          ><p class="tekstPitanja">{{ odgovor.tekst }}</p></NButton
        >
      </template>
    </section>
  </div>
</template>

<style>
.shake {
  animation: shake 0.82s cubic-bezier(0.36, 0.07, 0.19, 0.97) both;
  transform: translate3d(0, 0, 0);
}

.colorGreen {
  animation-name: colorGreen;
  animation-duration: 0.8s;
}

@keyframes colorGreen {
  0% {
    background-color: #000;
  }

  30% {
    background-color: green;
  }

  100% {
    background-color: green;
  }
}

@keyframes shake {
  10%,
  90% {
    transform: translate3d(-1px, 0, 0);
  }
  20%,
  80% {
    transform: translate3d(2px, 0, 0);
  }
  30%,
  50%,
  70% {
    transform: translate3d(-4px, 0, 0);
  }
  40%,
  60% {
    transform: translate3d(4px, 0, 0);
  }
}

.dugme {
  padding: 1.7rem 1rem;
  white-space: break-spaces;
}

.odgovori {
  display: flex;
  flex-direction: column;
  gap: 16px;
  color: black;
}
.pitanje {
  margin: 0.5em;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3rem;
  max-width: 100%;
}

.slikaPitanja {
  display: inline-block;
  border-radius: 25%;
  max-width: 100%;
  height: 200px;
}

.slikaPitanja img {
  max-width: 100%;
  max-height: 200px;
}
</style>
