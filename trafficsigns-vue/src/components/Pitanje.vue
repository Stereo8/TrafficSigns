<script setup lang="ts">
import { ref, watch } from "vue";
import { reactive } from "vue";
import { onMounted } from "vue";
import { NButton } from "naive-ui";

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

function checkOdgovor(odg: String) {
  if (odg == pitanje.value.tacan_odg) {
    emit("tacan");
  } else {
    emit("netacan");
  }
}

let p: Pitanje = await fetch(props.urlPitanja)
  .then((response) => response.json())
  .then((data) => data);

const pitanje = ref(p);

const slikaURL = ref(
  new String("http://localhost:8000/static/srbija/" + pitanje.value.znak)
);

const listaOdgovora = reactive({
  value: [
    pitanje.value.tacan_odg,
    pitanje.value.netacni_odg1,
    pitanje.value.netacni_odg2,
  ],
});

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
    slikaURL.value =
      "http://localhost:8000/static/srbija/" + pitanje.value.znak;
  }
);
</script>

<template>
  <div class="pitanje">
    <div class="slikaPitanja">
      <img :src="slikaURL" :alt="pitanje.opis" />
    </div>

    <section class="odgovori">
      <NButton @click="checkOdgovor(listaOdgovora.value[0])">{{
        listaOdgovora.value[0]
      }}</NButton>
      <NButton @click="checkOdgovor(listaOdgovora.value[1])">{{
        listaOdgovora.value[1]
      }}</NButton>
      <NButton @click="checkOdgovor(listaOdgovora.value[2])">{{
        listaOdgovora.value[2]
      }}</NButton>
    </section>
  </div>
</template>

<style>
NButton {
  overflow-wrap: break-word;
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
  gap: 5rem;
}

.slikaPitanja {
  display: inline-block;
  max-width: 100%;
  max-height: 400px;
}

.slikaPitanja img {
  max-width: 100%;
  height: auto;
}
</style>
