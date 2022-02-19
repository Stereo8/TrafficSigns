<script setup lang="ts">
import PitanjeVue from "@/components/Pitanje.vue";
import type { Pitanje } from "@/types/Pitanje";
import { computed, onMounted, reactive, ref } from "vue";
import { NInput, NSpin, NNotificationProvider } from "naive-ui";
import { useNotification } from "naive-ui";
import { getRandId } from "@/util";
import type { NotificationType } from "naive-ui";

const notification = useNotification();

const urlP = computed(
  () => `http://localhost:8000/znaci/pitanje/${idPitanja.value}`
);

const idPitanja = ref(getRandId().toString());

function tacanNotify() {
  notification.create({
    type: "success",
    title: "Tacan odgovor!",
    content: "Bravo!",
    closable: false,
    duration: 1000,
  });
  idPitanja.value = getRandId().toString();
}

function netacanNotify() {
  notification.create({
    type: "error",
    title: "Netacan odgovor!",
    content: "Ocajan si!",
    closable: false,
    duration: 1000,
  });
  idPitanja.value = getRandId().toString();
}
</script>

<template>
  <n-notification-provider>
    <Suspense>
      <template #default>
        <PitanjeVue
          :url-pitanja="urlP"
          @tacan="tacanNotify"
          @netacan="netacanNotify"
        ></PitanjeVue>
      </template>

      <template #fallback>
        <NSpin size="large" id="vrti"></NSpin>
      </template>
    </Suspense>
  </n-notification-provider>
</template>

<style>
#vrti {
  margin: auto;
}
</style>
