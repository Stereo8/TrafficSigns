import { defineStore } from "pinia";

export const useStore = defineStore("store", {
  state: () => {
    return {
      brPoena: 0,
      brTacnih: 0,
      brNetacnih: 0,
      tajmer: 0,
      stanje: "pocetak", // "pocetak" | "igra" | "kraj"
    };
  },
});
