<script setup lang="ts">
import { ref, watch } from "vue";
import { reactive } from "vue";
import { onMounted } from "vue";
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
const glowingRed = ref(false);
const glowingGreen = ref(false);

const listaOdgovora = reactive({
  value: [
    pitanje.value.tacan_odg,
    pitanje.value.netacni_odg1,
    pitanje.value.netacni_odg2,
  ],
});

function checkOdgovor(odg: String) {
  if (odg == pitanje.value.tacan_odg) {
    emit("tacan");
  } else {
    protresi();
    setTimeout(() => {
      emit("netacan");
    }, 1000);
  }
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
      pitanje.value.tacan_odg,
      pitanje.value.netacni_odg1,
      pitanje.value.netacni_odg2,
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
      />
    </div>

    <section class="odgovori">
      <template v-for="odgovor in listaOdgovora.value">
        <NButton @click="checkOdgovor(odgovor)"
          ><p class="tekstPitanja">{{ odgovor }}</p></NButton
        >
      </template>
    </section>
  </div>
</template>

<style>
.glowContainer {
  position: absolute;
  top: 50%;
  left: 50%;
  height: 100px;
  width: 100px;
  border-radius: 50%;
}
.tekstPitanja {
  overflow-wrap: break-word;
}

.shake {
  animation: shake 0.82s cubic-bezier(0.36, 0.07, 0.19, 0.97) both;
  transform: translate3d(0, 0, 0);
}

.glowRed {
  animation-name: glowRed;
  animation-duration: 0.8s;
}

.glowGreen {
  animation-name: glowGreen;
  animation-duration: 0.8s;
}

@keyframes glowRed {
  0% {
    box-shadow: 0 0 0 red;
  }

  50% {
    box-shadow: 0 0 60px red;
  }

  100% {
    box-shadow: 0 0 0 red;
  }
}

@keyframes glowGreen {
  0% {
    box-shadow: 0 0 0 green;
  }

  50% {
    box-shadow: 0 0 60px green;
  }

  100% {
    box-shadow: 0 0 0 green;
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

.odgovori {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.pitanje {
  margin: 0.5em;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3rem;
  max-width: 300px;
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
