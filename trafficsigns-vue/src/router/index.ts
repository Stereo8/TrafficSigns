import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("../views/GameView.vue"),
    },
    {
      path: "/pitanje",
      name: "pitanje",
      component: () => import("../components/Pitanje.vue"),
    },
    {
      path: "/noviHome",
      name: "noviHome",
      component: () => import("../views/StartView.vue"),
    },
  ],
});

export default router;
