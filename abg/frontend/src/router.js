import Vue from "vue";
import Router from "vue-router";
// import { Store } from "vuex";
Vue.use(Router);
let router = new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name:"home",
      props: true,
      component: () => import("./components/HomePage"),
      },
      {
        path: "/GalleryPage",
        name:"GalleryPage",
        props: true,
        component: () => import("./components/GalleryPage"),
        },
      {
        path: "/campaign1",
        name:"camp1",
        props: true,
        component: () => import("./components/CampaignOne"),
        },
        {
          path: "/ContactusPage",
          name:"ContactusPage",
          props: true,
          component: () => import("./components/ContactusPage"),
          },
          {
            path: "/CoursesPage",
            name:"CoursesPage",
            props: true,
            component: () => import("./components/CoursesPage"),
            },
          {
            path: "/AboutusPage",
            name:"AboutusPage",
            props: true,
            component: () => import("./components/AboutusPage"),
            },
            {
              path: "/CourseDetailedView",
              name:"CourseDetailedView",
              props: true,
              component: () => import("./components/CourseDetailedView"),
              },
 
  ],
  scrollBehavior() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0;
  },

});
// router.beforeEach((to, from, next) => {
//   if (
//     to.matched.some((route) => route.meta.requiresAuth == true) &&
//     store.state.isLoggedIn == false
//   ) {
//     console.log(from);
//     next({ name: "login", params: { lastPage: from } });
//     return;
//   }


//   next();
// });

export default router;
