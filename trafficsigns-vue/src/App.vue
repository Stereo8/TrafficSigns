<script setup lang="ts">
import { computed, ref } from "vue";
import { RouterLink, RouterView } from "vue-router";
import { NConfigProvider, useOsTheme, darkTheme, lightTheme } from "naive-ui";
import { useStore } from "@/stores/appState";
import { useRouter } from "vue-router";

const osThemeRef = useOsTheme();
const store = useStore();
const router = useRouter();
const screen = ref("pocetak");

const theme = computed(() => (osThemeRef.value === "dark" ? darkTheme : null));

router.replace("/pocetak");

store.$subscribe((mutation, state) => {
  if (screen.value == "pocetak" && state.stanje == "igra") {
    screen.value = "igra";
  } else if (screen.value == "igra" && state.stanje == "kraj") {
    screen.value = "kraj";
  } else if (screen.value == "kraj" && state.stanje == "pocetak") {
    screen.value = "pocetak";
  }
  router.replace("/" + screen.value);
});
</script>

<template>
  <NConfigProvider :theme="lightTheme">
    <RouterView></RouterView>
  </NConfigProvider>
</template>

<style>
@import "@/assets/base.css";

#app {
  display: flex;
  place-items: center;
}

body {
  display: flex;
  justify-content: center;
  background-image: url("http://localhost:8000/static/pozadina.jpg");
}
</style>
