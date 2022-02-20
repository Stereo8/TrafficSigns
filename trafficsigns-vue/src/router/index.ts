import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/pocetak",
      name: "pocetak",
      component: () => import("../views/StartView.vue"),
    },
    {
      path: "/igra",
      name: "igra",
      component: () => import("../views/GameView.vue"),
    },
    {
      path: "/kraj",
      name: "kraj",
      component: () => import("../views/EndView.vue"),
    },
  ],
});

export default router;
